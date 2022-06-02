# Optimum

## Information Gathering
10.10.10.8<br>
Optimum<br>

Software Versions
- HttpFileServer 2.3

## Enumeration
Start with an nmap scan as usual:
```bash
# Nmap 7.92 scan initiated Sun Feb 20 12:11:56 2022 as: nmap -sC -sV -oN nmap/optimum.nmap -Pn -p- 10.10.10.8
Nmap scan report for 10.10.10.8
Host is up (0.029s latency).
Not shown: 65534 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    HttpFileServer httpd 2.3
|_http-server-header: HFS 2.3
|_http-title: HFS /
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Feb 20 12:14:25 2022 -- 1 IP address (1 host up) scanned in 148.77 seconds

```
I also run a Nikto scan against port 80
```bash
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.10.8
+ Target Hostname:    10.10.10.8
+ Target Port:        80
+ Start Time:         2022-02-20 12:14:01 (GMT-5)
---------------------------------------------------------------------------
+ Server: HFS 2.3
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Cookie HFS_SID created without the httponly flag
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OSVDB-38019: /?mod=<script>alert(document.cookie)</script>&op=browse: Sage 1.0b3 is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.
+ 7864 requests: 0 error(s) and 5 item(s) reported on remote host
+ End Time:           2022-02-20 12:23:30 (GMT-5) (569 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

## Exploitation
This server has a CVE: CVE-2014-6287. The exploit-db PoC is here: https://www.exploit-db.com/exploits/39161<br> 
There is also a Metasploit module for this application which may be easier. I tried for so long to perform this exploit manually but was unsuccessful in my efforts.<br>
Search "httpfileserver" returns 1 exploit <b>exploit/windows/http/rejetto_hfs_exec</b>. Setting the options and running the exploit gives you foothold. The exploit does take a long time.
```
meterpreter > getuid
Server username: OPTIMUM\kostas
```

## Privilege Escalation
Backgrounding the process using "background". I search for "local_exploit" and use the <b>post/multi/recon/local_exploit_suggester</b>. After running and waiting a minute, I get back two potential exploits:
```
[*] 10.10.10.8 - Collecting local exploits for x86/windows...
[*] 10.10.10.8 - 40 exploit checks are being tried...
[+] 10.10.10.8 - exploit/windows/local/bypassuac_eventvwr: The target appears to be vulnerable.
[+] 10.10.10.8 - exploit/windows/local/ms16_032_secondary_logon_handle_privesc: The service is running, but could not be validated.
[*] Post module execution completed
```
<b>exploit/windows/local/ms16_032_secondary_logon_handle_privesc</b> is the exploit that gives me Administrator.
```
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
```