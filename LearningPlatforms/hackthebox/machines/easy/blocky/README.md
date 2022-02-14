# Blocky

## Information Gathering
Blocky<br>
10.10.10.37<br>

<ul>Software Version
	<li>ProFTPD 1.3.5a</li>
	<li>OpenSSH 7.2p2 Ubuntu 4ubuntu2.2</li>
	<li>Apache httpd 2.4.18</li>
	<li>WordPress 4.8</li>
</ul>

## Enumeration
Start with an nmap scan of course:
```bash
# Nmap 7.92 scan initiated Sun Feb 13 20:21:35 2022 as: nmap -p- -A -oN nmap/all_ports.nmap 10.10.10.37
Nmap scan report for 10.10.10.37
Host is up (0.030s latency).
Not shown: 65530 filtered tcp ports (no-response)
PORT      STATE  SERVICE   VERSION
21/tcp    open   ftp       ProFTPD 1.3.5a
22/tcp    open   ssh       OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 d6:2b:99:b4:d5:e7:53:ce:2b:fc:b5:d7:9d:79:fb:a2 (RSA)
|   256 5d:7f:38:95:70:c9:be:ac:67:a0:1e:86:e7:97:84:03 (ECDSA)
|_  256 09:d5:c2:04:95:1a:90:ef:87:56:25:97:df:83:70:67 (ED25519)
80/tcp    open   http      Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: BlockyCraft &#8211; Under Construction!
|_http-generator: WordPress 4.8
8192/tcp  closed sophos
25565/tcp open   minecraft Minecraft 1.11.2 (Protocol: 127, Message: A Minecraft Server, Users: 0/20)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Feb 13 20:23:29 2022 -- 1 IP address (1 host up) scanned in 113.84 seconds
```
Becuase there is a HTTP server, I run Nikto and a directory buster
```bash
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.37
+ Target Port: 80
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET Uncommon header 'link' found, with contents: <http://10.10.10.37/index.php/wp-json/>; rel="https://api.w.org/"
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ HEAD Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ TUXNAKES Web Server returns a valid response with junk HTTP methods, this may cause false positives.
+ DEBUG DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ GET Uncommon header 'x-ob_mode' found, with contents: 1
+ OSVDB-3233: GET /icons/README: Apache default file found.
+ GET /wp-content/plugins/akismet/readme.txt: The WordPress Akismet plugin 'Tested up to' version usually matches the WordPress version
+ GET /wp-links-opml.php: This WordPress script reveals the installed version.
+ OSVDB-3092: GET /license.txt: License file found may identify site software.
+ GET /: A Wordpress installation was found.
+ GET /phpmyadmin/: phpMyAdmin directory found
+ GET Cookie wordpress_test_cookie created without the httponly flag
+ OSVDB-3268: GET /wp-content/uploads/: Directory indexing found.
+ GET /wp-content/uploads/: Wordpress uploads directory is browsable. This may reveal sensitive information
+ GET /wp-login.php: Wordpress login found
```
Directory Busting
```bash
--------------------------------
Files found during testing:

Files found with a 200 responce:

/wp-login.php
/plugins/assets/js/script.js
/wp-includes/js/jquery/jquery-migrate.min.js
/wp-includes/js/jquery/jquery.js
/wp-content/themes/twentyseventeen/assets/js/skip-link-focus-fix.js
/wp-content/themes/twentyseventeen/assets/js/global.js
/wp-content/themes/twentyseventeen/assets/js/jquery.scrollTo.js
/wp-includes/js/wp-embed.min.js
/plugins/files/BlockyCore.jar
/wp-includes/js/jquery/jquery-migrate.js
/plugins/files/griefprevention-1.11.2-3.1.1.298.jar
/wp-includes/js/jquery/jquery.color.min.js
/wp-content/themes/twentyseventeen/assets/js/customize-controls.js
/wp-includes/js/jquery/jquery.form.js
/wp-includes/js/jquery/jquery.form.min.js
/wp-content/themes/twentyseventeen/assets/js/customize-preview.js
/wp-includes/js/jquery/jquery.hotkeys.js
/wp-includes/js/jquery/jquery.hotkeys.min.js
/wp-content/themes/twentyseventeen/assets/js/navigation.js
/wp-includes/js/jquery/jquery.masonry.min.js
/wp-includes/js/jquery/jquery.query.js
/wp-content/themes/twentyseventeen/assets/images/svg-icons.svg
/plugins/assets/css/styles.css
/wp-includes/js/jquery/jquery.schedule.js
/wp-includes/js/jquery/jquery.serialize-object.js
/wp-content/themes/twentyseventeen/assets/js/html5.js

```
Taking a look at the actual site, it seems to be a wordpress site. So I also run wpscan
```bash
wpscan --url http://10.10.10.37/ -e ap,at,u --plugins-detection aggressive -f cli-no-color -o wp/blocky.wp

_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.20
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://10.10.10.37/ [10.10.10.37]
[+] Started: Sun Feb 13 20:48:35 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.18 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://10.10.10.37/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://10.10.10.37/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://10.10.10.37/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://10.10.10.37/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 4.8 identified (Insecure, released on 2017-06-08).
 | Found By: Rss Generator (Passive Detection)
 |  - http://10.10.10.37/index.php/feed/, <generator>https://wordpress.org/?v=4.8</generator>
 |  - http://10.10.10.37/index.php/comments/feed/, <generator>https://wordpress.org/?v=4.8</generator>

[+] WordPress theme in use: twentyseventeen
 | Location: http://10.10.10.37/wp-content/themes/twentyseventeen/
 | Last Updated: 2021-07-22T00:00:00.000Z
 | Readme: http://10.10.10.37/wp-content/themes/twentyseventeen/README.txt
 | [!] The version is out of date, the latest version is 2.8
 | Style URL: http://10.10.10.37/wp-content/themes/twentyseventeen/style.css?ver=4.8
 | Style Name: Twenty Seventeen
 | Style URI: https://wordpress.org/themes/twentyseventeen/
 | Description: Twenty Seventeen brings your site to life with header video and immersive featured images. With a fo...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.3 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://10.10.10.37/wp-content/themes/twentyseventeen/style.css?ver=4.8, Match: 'Version: 1.3'


[i] No plugins Found.


```

## Exploitation
This box actually teaches how to enumerate a wordpress web application pretty well. Wordpress is full of directories and subdirectories. If you do it incorrectly, you may end up with a whole bunch of nothing. When scanning with dirbuster, only looking at directories gives you quality results. Through directory busting, I find /plugins/files/BlockyCore.jar. Downloading this file and decompressing it gives a file BlockyCore.class. Decompiling this file gives:
```java
package com.myfirstplugin;

public class BlockyCore
{
    public String sqlHost;
    public String sqlUser;
    public String sqlPass;
    
    public BlockyCore() {
        this.sqlHost = "localhost";
        this.sqlUser = "root";
        this.sqlPass = "8YsqfCTnvxAUeduzjNSXe22";
    }
    
    public void onServerStart() {
    }
    
    public void onServerStop() {
    }
    
    public void onPlayerJoin() {
        this.sendMessage("TODO get username", "Welcome to the BlockyCraft!!!!!!!");
    }
    
    public void sendMessage(final String username, final String message) {
    }
}
```
Which exposes a password for phpmyadmin. I accessed phpmyadmin and found one user in the wp_user table with the username notch and a password hash of $P$BiVoTj899ItS1EZnMhqeqVbrZI4Oq0/. I tried for so long to crack this password but couldn't. So I used the exposed password with notch to SSH in. This gives you foothold.

## Privilege Escalation
The privilege escalation for this box was very straight forward. If you use:
```bash
sudo -l

User notch may run the following commands on Blocky:
    (ALL : ALL) ALL
```
Which means you can use sudo -i and instantly get root shell.