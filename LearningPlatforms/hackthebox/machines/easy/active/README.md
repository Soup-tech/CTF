# Active

## Information Gathering
Active<br>
10.10.10.100<br>

Software Versions

## Enumeration
Of course start with your nmap scan:
```bash
# Nmap 7.92 scan initiated Tue Feb 22 13:21:40 2022 as: nmap -sC -sV -oN nmap/active.nmap -Pn 10.10.10.100
Nmap scan report for 10.10.10.100
Host is up (0.030s latency).
Not shown: 986 closed tcp ports (reset)
PORT      STATE SERVICE       VERSION
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-02-22 18:28:51Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown
49155/tcp open  unknown
49157/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49158/tcp open  unknown
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
| smb2-security-mode: 
|   2.1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Feb 22 13:22:51 2022 -- 1 IP address (1 host up) scanned in 71.29 seconds

```
Seems like we are working with Microsoft technology, specifically Active Directory (the name of the box is Active, duh...).<br>
I first start enumerating using enum4linux and smbmap to see if anything is open or exposed. From enum4linux, we see an exposed shares when no credentials are supplied.
```bash
smbmap -u "" -p "" -P 445 -H 10.10.10.100
[+] IP: 10.10.10.100:445        Name: 10.10.10.100                                      
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    NO ACCESS       Remote IPC
        NETLOGON                                                NO ACCESS       Logon server share 
        Replication                                             READ ONLY
        SYSVOL                                                  NO ACCESS       Logon server share 
        Users                                                   NO ACCESS

```
I also run Kerbrute to enumerate users.
```bash
./kerbrute_linux_amd64 userenum --dc 10.10.10.100 -d active.htb ~/Downloads/users.txt

2022/02/22 14:18:24 >  [+] VALID USERNAME:       administrator@active.htb
2022/02/22 14:18:59 >  [+] VALID USERNAME:       Administrator@active.htb
```
Only getting back administrator.<br>
I look through the open "Replication" share for a while and stumble upon Groups.xml. Inside shows some pretty good information about a user SVG_TGS (I think) with a potential password.
## Exploitation

## Privilege Escalation
