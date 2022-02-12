# SwagShop

## Information Gathering
10.10.10.140
SwagShop



## Enumeration
Nmap scan:<br>
```bash
sudo nmap -A -O -p- nmap/swagshop_aggr.nmap 10.10.10.140
Starting Nmap 7.92 ( https://nmap.org ) at 2022-01-19 21:47 EST
Unable to split netmask from target expression: "nmap/swagshop_aggr.nmap"
Nmap scan report for 10.10.10.140
Host is up (0.030s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b6:55:2b:d2:4e:8f:a3:81:72:61:37:9a:12:f6:24:ec (RSA)
|   256 2e:30:00:7a:92:f0:89:30:59:c1:77:56:ad:51:c0:ba (ECDSA)
|_  256 4c:50:d5:f2:70:c5:fd:c4:b2:f0:bc:42:20:32:64:34 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Did not follow redirect to http://swagshop.htb/
|_http-server-header: Apache/2.4.18 (Ubuntu)
Aggressive OS guesses: Linux 3.12 (95%), Linux 3.13 (95%), Linux 3.2 - 4.9 (95%), Linux 3.8 - 3.11 (95%), Linux 4.4 (95%), Linux 3.16 (95%), Linux 3.18 (95%), Linux 4.2 (95%), Linux 4.8 (95%), ASUS RT-N56U WAP (Linux 3.4) (95%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 8080/tcp)
HOP RTT      ADDRESS
1   27.21 ms 10.10.14.1
2   27.38 ms 10.10.10.140

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 42.34 seconds
```
Nikto scan:<br>
```bash
nikto -Host 10.10.10.140 -Format txt -o swagshop.nikto
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.140
+ Target Port: 80
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ HEAD Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ OSVDB-39272: GET /favicon.ico file identifies this app/server as: Magento Go CMS
+ OSVDB-3268: GET /app/: Directory indexing found.
+ OSVDB-3092: GET /app/: This might be interesting...
+ OSVDB-3268: GET /includes/: Directory indexing found.
+ OSVDB-3092: GET /includes/: This might be interesting...
+ OSVDB-3268: GET /lib/: Directory indexing found.
+ OSVDB-3092: GET /lib/: This might be interesting...
+ OSVDB-3092: GET /install.php: install.php file found.
+ OSVDB-3092: GET /LICENSE.txt: License file found may identify site software.
+ OSVDB-3233: GET /icons/README: Apache default file found.
+ GET /RELEASE_NOTES.txt: A database error may reveal internal details about the running database.
+ GET /RELEASE_NOTES.txt: Magento Shop Changelog identified.
+ GET /skin/adminhtml/default/default/media/editor.swf: Several Adobe Flash files that ship with Magento are vulnerable to DOM based Cross Site Scripting (XSS). See http://appcheck-ng.com/unpatched-vulnerabilites-in-magento-e-commerce-platform/
+ GET /skin/adminhtml/default/default/media/uploader.swf: Several Adobe Flash files that ship with Magento are vulnerable to DOM based Cross Site Scripting (XSS). See http://appcheck-ng.com/unpatched-vulnerabilites-in-magento-e-commerce-platform/
+ GET /skin/adminhtml/default/default/media/uploaderSingle.swf: Several Adobe Flash files that ship with Magento are vulnerable to DOM based Cross Site Scripting (XSS). See http://appcheck-ng.com/unpatched-vulnerabilites-in-magento-e-commerce-platform/
```
Gobuster scan:<br>
```bash
gobuster dir -u http://10.10.10.140 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 20 -x html,php,txt -o gob/swagshop.gob
/media                (Status: 301) [Size: 312] [--> http://10.10.10.140/media/]
/index.php            (Status: 302) [Size: 0] [--> http://swagshop.htb/]
/includes             (Status: 301) [Size: 315] [--> http://10.10.10.140/includes/]
/lib                  (Status: 301) [Size: 310] [--> http://10.10.10.140/lib/]
/install.php          (Status: 200) [Size: 44]
/app                  (Status: 301) [Size: 310] [--> http://10.10.10.140/app/]
/js                   (Status: 301) [Size: 309] [--> http://10.10.10.140/js/]
/api.php              (Status: 200) [Size: 37]
/shell                (Status: 301) [Size: 312] [--> http://10.10.10.140/shell/]
/skin                 (Status: 301) [Size: 311] [--> http://10.10.10.140/skin/]
/cron.php             (Status: 200) [Size: 0]
/LICENSE.html         (Status: 200) [Size: 10679]
/LICENSE.txt          (Status: 200) [Size: 10410]
/var                  (Status: 301) [Size: 310] [--> http://10.10.10.140/var/]
/errors               (Status: 301) [Size: 313] [--> http://10.10.10.140/errors/]
/mage                 (Status: 200) [Size: 1319]
/server-status        (Status: 403) [Size: 300]
```

## Exploitation
Webserver - Magento 1.7.0.2: 

## Privilege Escalation
