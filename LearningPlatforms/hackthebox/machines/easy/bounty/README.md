# Bounty

## Information Gathering
10.10.10.93
Bounty
Windows


## Enumeration
Determine what services are running on this machine.
```bash
# Nmap 7.92 scan initiated Wed Jan 12 14:58:03 2022 as: nmap -sC -sV -oN nmap/bounty.nmap -Pn 10.10.10.93
Nmap scan report for 10.10.10.93
Host is up (0.028s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 7.5
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Bounty
|_http-server-header: Microsoft-IIS/7.5
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jan 12 14:58:15 2022 -- 1 IP address (1 host up) scanned in 12.04 seconds
```
Because there is only a webserver, I'll also run other enumeartion scripts
```bash

```

Allowed file extensions
.config
.jpg
.png
.gif

Configurations:
Content-type: image/gif ; filename: pwn.aspx%00.gif ; 
Content-type: image/gif ; filename: pwn.aspx ; Magic-bytes: GIF89a; ;


## Exploitation

## Priv Esc