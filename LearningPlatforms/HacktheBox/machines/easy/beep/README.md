# Beep

## Information Gathering
Beep<br>
10.10.10.7<br>

<ul>Software Versions
	<li>OpenSSH 4.3</li>
	<li>Apache httpd 2.2.3</li>
	<li>Cyrus pop3d 2.3.7-Invoca-RPM-2.3.7-7.el5_6.4</li>
	<li>MiniServ/1.570</li>
	<li>HylaFAX 4.3.10</li>
	<li>FreePBX 2.8.1.4</li>
</ul>

## Enumeration
Start with the nmap scan:<br>
```bash
# Nmap 7.92 scan initiated Mon Feb 14 18:34:23 2022 as: nmap -p- -A -oN nmap/all_ports.nmap -Pn 10.10.10.7
Nmap scan report for 10.10.10.7
Host is up (0.028s latency).
Not shown: 65519 closed tcp ports (reset)
PORT      STATE SERVICE    VERSION
22/tcp    open  ssh        OpenSSH 4.3 (protocol 2.0)
| ssh-hostkey: 
|   1024 ad:ee:5a:bb:69:37:fb:27:af:b8:30:72:a0:f9:6f:53 (DSA)
|_  2048 bc:c6:73:59:13:a1:8a:4b:55:07:50:f6:65:1d:6d:0d (RSA)
25/tcp    open  smtp       Postfix smtpd
|_smtp-commands: beep.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, ENHANCEDSTATUSCODES, 8BITMIME, DSN
80/tcp    open  http       Apache httpd 2.2.3
|_http-server-header: Apache/2.2.3 (CentOS)
|_http-title: Did not follow redirect to https://10.10.10.7/
110/tcp   open  pop3       Cyrus pop3d 2.3.7-Invoca-RPM-2.3.7-7.el5_6.4
|_pop3-capabilities: USER UIDL EXPIRE(NEVER) PIPELINING RESP-CODES LOGIN-DELAY(0) STLS IMPLEMENTATION(Cyrus POP3 server v2) AUTH-RESP-CODE APOP TOP
111/tcp   open  rpcbind    2 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2            111/tcp   rpcbind
|   100000  2            111/udp   rpcbind
|   100024  1            875/udp   status
|_  100024  1            878/tcp   status
143/tcp   open  imap       Cyrus imapd 2.3.7-Invoca-RPM-2.3.7-7.el5_6.4
|_imap-capabilities: Completed RIGHTS=kxte QUOTA X-NETSCAPE NAMESPACE OK IMAP4rev1 THREAD=ORDEREDSUBJECT THREAD=REFERENCES IMAP4 ATOMIC SORT UIDPLUS SORT=MODSEQ UNSELECT BINARY NO CATENATE CHILDREN ACL ANNOTATEMORE MULTIAPPEND STARTTLS CONDSTORE LISTEXT URLAUTHA0001 LITERAL+ IDLE LIST-SUBSCRIBED RENAME MAILBOX-REFERRALS ID
443/tcp   open  ssl/http   Apache httpd 2.2.3 ((CentOS))
|_ssl-date: 2022-02-15T00:45:06+00:00; +1h06m56s from scanner time.
|_http-server-header: Apache/2.2.3 (CentOS)
| ssl-cert: Subject: commonName=localhost.localdomain/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Not valid before: 2017-04-07T08:22:08
|_Not valid after:  2018-04-07T08:22:08
|_http-title: Elastix - Login page
878/tcp   open  status     1 (RPC #100024)
993/tcp   open  ssl/imap   Cyrus imapd
|_imap-capabilities: CAPABILITY
995/tcp   open  pop3       Cyrus pop3d
3306/tcp  open  mysql      MySQL (unauthorized)
4190/tcp  open  sieve      Cyrus timsieved 2.3.7-Invoca-RPM-2.3.7-7.el5_6.4 (included w/cyrus imap)
4445/tcp  open  upnotifyp?
4559/tcp  open  hylafax    HylaFAX 4.3.10
5038/tcp  open  asterisk   Asterisk Call Manager 1.1
10000/tcp open  http       MiniServ 1.570 (Webmin httpd)
|_http-title: Site doesnt have a title (text/html; Charset=iso-8859-1).
```
There is a web server so I run Nikto and directory busting
```bash
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.7
+ Target Port: 80
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ HEAD Apache/2.2.3 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ OSVDB-877: TRACE HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ OSVDB-3268: GET /icons/: Directory indexing found.
+ GET Server may leak inodes via ETags, header found with file /icons/README, inode: 884871, size: 4872, mtime: Thu Jun 24 15:46:08 2010
+ OSVDB-3233: GET /icons/README: Apache default file found.
```
There are a few webservers running on this server so I'm gonna do a whoooooole bunch of directory busting. Because I'm enumerating a lot of web servers, I'm gonna go with Gobuster because it does not use recursion.<br>
The first webserver I enumerate is port 80 which immediatly redirects to the HTTPS server.
```bash
/images               (Status: 301) [Size: 310] [--> https://10.10.10.7/images/]
/index.php            (Status: 200) [Size: 1785]
/help                 (Status: 301) [Size: 308] [--> https://10.10.10.7/help/]
/themes               (Status: 301) [Size: 310] [--> https://10.10.10.7/themes/]
/register.php         (Status: 200) [Size: 1785]
/modules              (Status: 301) [Size: 311] [--> https://10.10.10.7/modules/]
/mail                 (Status: 301) [Size: 308] [--> https://10.10.10.7/mail/]
/admin                (Status: 301) [Size: 309] [--> https://10.10.10.7/admin/]
/static               (Status: 301) [Size: 310] [--> https://10.10.10.7/static/]
/lang                 (Status: 301) [Size: 308] [--> https://10.10.10.7/lang/]
/config.php           (Status: 200) [Size: 1785]
/robots.txt           (Status: 200) [Size: 28]
```
When navigating to /admin, I am presented with a restricted page which needs credentials. After a few tries, I get an unauthorization message. However, the header of the application is exposed which reveals the version of FreePBX. Nice!<br><br>
## Exploitation
The first method uses this exploit: https://www.exploit-db.com/exploits/37637 <br>
This page leaks credentials to the server which allows you to login as root over ssh. 
