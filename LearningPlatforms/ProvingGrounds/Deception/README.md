# Deception

## Information Gathering
Deception
192.168.240.34

Software Versions
- OpenSSH 7.6p1
- Apache httpd 2.4.29
- phpmyadmin
- WordPress version 5.3.2

Users
- yash:
- haclabs

## Scanning
Start out with the AutoRecon scan. The full TCP scan came back:
```bash
# Nmap 7.92 scan initiated Sun Apr 10 00:03:03 2022 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/_full_tcp_nmap.txt -oX /home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/xml/_full_tcp_nmap.xml 192.168.240.34
Nmap scan report for 192.168.240.34
Host is up, received user-set (0.047s latency).
Scanned at 2022-04-10 00:03:03 EDT for 66s
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9d:d0:98:da:0d:32:3d:0b:3f:42:4d:d7:93:4f:fd:60 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLSsGJtpg5KvawG56yanORlHOGP7anzFKXq8ZDjuBD20sWrHl6g0J1+w497SyvRnB6EDOBGrjqlEXqlI7DvgrAo08GOCvoajuPpitLuC2rCfRC3b3ctn/n2+zGkkfsD5Y0U6PQrchRNpMKH/4nsaBcrTV8ZkEGF+VNYhnTO7c1vGhpH0i5c7UzyKvfqz/KzH4YryUpC1opxB9pn0jHH+iQ8H+Brne/bvOmpyvoy84CzuunshxMmAV9qdaLmZxOOF25SF5uHh6r1h8tVG8yLbD1N7IfPXXy0GpZZZIBt4i/ZQVpfk1i0GsY4/mL3VCrtFsO4p2PxRLVws5Fpces+pDN
|   256 4c:f4:2e:24:82:cf:9c:8d:e2:0c:52:4b:2e:a5:12:d9 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDwKM2aO1LW/C4gfLHyFmkrfcPcXVHvIEK8JN9pk/9kNhZKz8X9byyxiWMnNS/6AQNMAV0d5B+d0/VK2eps90ZI=
|   256 a9:fb:e3:f4:ba:d6:1e:72:e7:97:25:82:87:6e:ea:01 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEOULyvRe2blVRaHM9twRKyE34SQUyGPMjVmRv2srgvv
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
Aggressive OS guesses: Linux 2.6.32 (91%), Linux 2.6.32 or 3.10 (91%), Linux 3.5 (91%), WatchGuard Fireware 11.8 (91%), Synology DiskStation Manager 5.1 (90%), Linux 2.6.35 (90%), Linux 2.6.39 (90%), Linux 3.10 - 3.12 (90%), Linux 4.2 (90%), Linux 4.4 (90%)

```

Looking through the tcp_80_http_nmap.txt, there appears to be a wordpress blog in /wordpress/. phpmyadmin is also accessible from the web applicaiton.
Because there is a wordpress blog running, I enumerate it using the recommended command in \_manual_commands.txt
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

[+] URL: http://192.168.240.34/wordpress/ [192.168.240.34]
[+] Started: Sun Apr 10 00:13:29 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.29 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://192.168.240.34/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://192.168.240.34/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://192.168.240.34/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://192.168.240.34/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.3.2 identified (Insecure, released on 2019-12-18).
 | Found By: Emoji Settings (Passive Detection)
 |  - http://192.168.240.34/wordpress/, Match: 'wp-includes\/js\/wp-emoji-release.min.js?ver=5.3.2'
 | Confirmed By: Meta Generator (Passive Detection)
 |  - http://192.168.240.34/wordpress/, Match: 'WordPress 5.3.2'

[i] The main theme could not be detected.

[+] Enumerating Vulnerable Plugins (via Aggressive Methods)

 Checking Known Locations -: |============================================================================================================================================================================================================|
[+] Checking Plugin Versions (via Aggressive Methods)

[i] No plugins Found.

[+] Enumerating Vulnerable Themes (via Passive and Aggressive Methods)

 Checking Known Locations -: |============================================================================================================================================================================================================|

[i] No themes Found.

[+] Enumerating Timthumbs (via Passive and Aggressive Methods)

 Checking Known Locations -: |============================================================================================================================================================================================================|

[i] No Timthumbs Found.

[+] Enumerating Config Backups (via Passive and Aggressive Methods)

 Checking Config Backups -: |=============================================================================================================================================================================================================|

[i] No Config Backups Found.

[+] Enumerating DB Exports (via Passive and Aggressive Methods)

 Checking DB Exports -: |=================================================================================================================================================================================================================|

[i] No DB Exports Found.

[+] Enumerating Medias (via Passive and Aggressive Methods) (Permalink setting must be set to "Plain" for those to be detected)

 Brute Forcing Attachment IDs -: |========================================================================================================================================================================================================|

[i] No Medias Found.

[+] Enumerating Users (via Passive and Aggressive Methods)

 Brute Forcing Author IDs -: |============================================================================================================================================================================================================|

[i] User(s) Identified:

[+] yash
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] haclabs
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Sun Apr 10 00:14:56 2022
[+] Requests Done: 6644
[+] Cached Requests: 4
[+] Data Sent: 1.93 MB
[+] Data Received: 1.075 MB
[+] Memory used: 222.512 MB
[+] Elapsed time: 00:01:26

```

Looking through the wordpress site, every single link redirects to "localhost/wordpres/some.php" which makes me think this WordPress installation is not complete. Looking at my Ferox scan, there are a few URL's that can be accessed.

```bash
200      GET       15l       74w     3338c http://192.168.240.34/icons/ubuntu-logo.png
200      GET      375l      981w    11026c http://192.168.240.34/index.html
200      GET      375l      981w    11026c http://192.168.240.34/index.html
200      GET       86l      288w     4914c http://192.168.240.34/wordpress/wp-login.php
200      GET      385l     3179w    19935c http://192.168.240.34/wordpress/license.txt
200      GET       98l      838w     7368c http://192.168.240.34/wordpress/readme.html
200      GET        2l        3w       22c http://192.168.240.34/wordpress/robots.txt
200      GET       20l       44w      418c http://192.168.240.34/wordpress/robots.html
200      GET        5l       15w      135c http://192.168.240.34/wordpress/wp-trackback.php
200      GET       17l       85w     1391c http://192.168.240.34/wordpress/wp-admin/install.php
200      GET       26l       93w     1491c http://192.168.240.34/wordpress/wp-admin/upgrade.php
```

Of which robots.html and robots.txt look interesting.

On index.html
API old0 : 5F4DCC3B5AA765D61D8327DEB882CF99