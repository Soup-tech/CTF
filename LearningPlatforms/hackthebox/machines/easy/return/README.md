# Return

## Information Gathering
Return<br>
10.10.11.108

## Recon
Start with the nmap scan:
```bash
Starting Nmap 7.92 ( https://nmap.org ) at 2022-02-07 17:24 EST
Nmap scan report for 10.10.11.108
Host is up (0.030s latency).
Not shown: 992 closed tcp ports (reset)
PORT    STATE SERVICE       VERSION
88/tcp  open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-02-07 22:50:28Z)
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: return.local0., Site: Default-First-Site-Name)
445/tcp open  microsoft-ds?
464/tcp open  kpasswd5?
593/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp open  tcpwrapped
Service Info: Host: PRINTER; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2022-02-07T22:50:33
|_  start_date: N/A
|_clock-skew: 25m31s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.12 seconds
```

## Exploitation

## Privilege Escalation