# Grandpa

## Information Gathering
10.10.10.14
Grandpa

## Enumeration and Scanning
Ran an nmap scan on the host<br>
```bash
# Nmap 7.92 scan initiated Tue Jan  4 21:59:44 2022 as: nmap -sC -sV -oN nmap/grandpa.nmap -Pn 10.10.10.14
Nmap scan report for 10.10.10.14
Host is up (0.053s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 6.0
|_http-title: Under Construction
|_http-server-header: Microsoft-IIS/6.0
| http-methods: 
|_  Potentially risky methods: TRACE COPY PROPFIND SEARCH LOCK UNLOCK DELETE PUT MOVE MKCOL PROPPATCH
| http-webdav-scan: 
|   Server Type: Microsoft-IIS/6.0
|   Allowed Methods: OPTIONS, TRACE, GET, HEAD, COPY, PROPFIND, SEARCH, LOCK, UNLOCK
|   WebDAV type: Unknown
|   Server Date: Wed, 05 Jan 2022 03:14:51 GMT
|_  Public Options: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jan  4 22:00:03 2022 -- 1 IP address (1 host up) scanned in 18.61 seconds
```

## Exploitation

## Privilege Escalation