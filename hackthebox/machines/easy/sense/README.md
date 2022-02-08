# Sense

## Information Gathering
10.10.10.60<br>
Sense

## Recon
Start with nmap scan:<br>
```bash
# Nmap 7.92 scan initiated Mon Feb  7 19:21:52 2022 as: nmap -sC -sV -oN nmap/sense.nmap 10.10.10.60
Nmap scan report for 10.10.10.60
Host is up (0.093s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
80/tcp  open  http     lighttpd 1.4.35
|_http-title: Did not follow redirect to https://10.10.10.60/
|_http-server-header: lighttpd/1.4.35
443/tcp open  ssl/http lighttpd 1.4.35
|_http-title: Login
| ssl-cert: Subject: commonName=Common Name (eg, YOUR name)/organizationName=CompanyName/stateOrProvinceName=Somewhere/countryName=US
| Not valid before: 2017-10-14T19:21:35
|_Not valid after:  2023-04-06T19:21:35
|_ssl-date: TLS randomness does not represent time
|_http-server-header: lighttpd/1.4.35

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Feb  7 19:22:26 2022 -- 1 IP address (1 host up) scanned in 33.53 seconds
```
Going to the http server automatically redirects us to the https server. I begin directory busting and running a quick nikto scan:<br>
```bash
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.60
+ Target Port: 80
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ GET Cookie PHPSESSID created without the httponly flag
+ OPTIONS Allowed HTTP Methods: OPTIONS, GET, HEAD, POST 
```
And the results from dirbuster:<br>
```
DirBuster 1.0-RC1 - Report
http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project
Report produced on Mon Feb 07 20:14:13 EST 2022
--------------------------------

https://10.10.10.60:443
--------------------------------
Directories found during testing:

Dirs found with a 200 response:

/
/tree/

Dirs found with a 302 response:

/installer/


--------------------------------
Files found during testing:

Files found with a 200 responce:

/index.html
/index.php
/help.php
/stats.php
/themes/pfsense_ng/javascript/niftyjsCode.js
/csrf/csrf-magic.js
/javascript/jquery.js
/edit.php
/license.php
/system.php
/status.php
/changelog.txt
/exec.php
/graph.php
/tree/index.html
/tree/tree.js
/wizard.php
/pkg.php
/system-users.txt

Files found with a 302 responce:

/installer/index.php

--------------------------------
```
Looking at Changelog.txt shows the following:
```
# Security Changelog 

### Issue
There was a failure in updating the firewall. Manual patching is therefore required

### Mitigated
2 of 3 vulnerabilities have been patched.

### Timeline
The remaining patches will be installed during the next maintenance window
```
There is also a text file system-users.txt which contains credentials
```
####Support ticket###

Please create the following user


username: Rohit
password: company defaults
```
Now that we are authenticated, I can see the version of pfsense that is running. I can also see what version of OpenBSD is running on the server
<ul>
	<li>pfsense 2.1.3-RELEASE</li>
	<li>FreeBSD 8.3-RELEASE-p16</li>
</ul>

## Exploitation
There are a few exploits in Metasploit for this. I use the <b>exploit/unix/http/pfsense_graph_injection_exec</b> which drops you directly into a root shell getting you both user and root flags.

