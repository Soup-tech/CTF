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
> After finding Santa's account, what is their position at the company?
```
The Boss!
```
> After finding McStocker's account, what is their position in the company?
```
Build Manager
```
> After finding the account responsible for tampering, what is their position in the company?
```
Mischief Manager
```
> What is the received flag when McSkidy fixes the Inventory Management System?
```
THM{AOC_IDOR_2B34BHI3}
```

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

> What is the name of the new cookie that was created for your account?
user-auth
> What encoding type was used for the cookie value?
```hexadecimal```
> What object format is the data of the cookie stored in?
```JSON```
> What is the value of the administrator cookie? (username = admin)
```7b636f6d70616e793a2022546865204265737420466573746976616c20436f6d70616e79222c206973726567697374657265643a2254727565222c20757365726e616d653a2261646d696e227d```
> What team environment is not responding?
```HR```
> What team environment is not responding?
```Application```

### Conclusion
Learn more about authentication bypass here: https://tryhackme.com/jr/authenticationbypass  
