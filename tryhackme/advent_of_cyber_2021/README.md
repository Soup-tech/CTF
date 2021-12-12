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

