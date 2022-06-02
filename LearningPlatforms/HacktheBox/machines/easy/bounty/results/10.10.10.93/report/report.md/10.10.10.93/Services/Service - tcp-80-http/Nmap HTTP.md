```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.10.93
```

[/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/tcp80/tcp_80_http_nmap.txt](file:///home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.92 scan initiated Fri May 20 15:44:41 2022 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/tcp80/tcp_80_http_nmap.txt -oX /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/tcp80/xml/tcp_80_http_nmap.xml 10.10.10.93
Nmap scan report for 10.10.10.93
Host is up, received user-set (0.046s latency).
Scanned at 2022-05-20 15:44:41 EDT for 120s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON          VERSION
80/tcp open  http    syn-ack ttl 127 Microsoft IIS httpd 7.5
|_http-title: Bounty
|_http-exif-spider: ERROR: Script execution failed (use -d to debug)
| http-vhosts: 
|_128 names had status 200
|_http-chrono: Request times for /; avg: 176.37ms; min: 154.54ms; max: 207.26ms
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1; jpg: 1
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    Other: 1; jpg: 1
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-config-backup: ERROR: Script execution failed (use -d to debug)
|_http-server-header: Microsoft-IIS/7.5
|_http-feed: Couldn't find any feeds.
|_http-mobileversion-checker: No mobile version detected.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-devframework: ASP.NET detected. Found related header.
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Allowed User Agents: 
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-errors: Couldn't find any error pages.
| http-php-version: Logo query returned unknown hash 270992517419489e60363688b0d9f352
|_Credits query returned unknown hash 270992517419489e60363688b0d9f352
|_http-date: Fri, 20 May 2022 19:45:34 GMT; +46s from local time.
|_http-malware-host: Host appears to be clean
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
| http-headers: 
|   Content-Length: 630
|   Content-Type: text/html
|   Last-Modified: Thu, 31 May 2018 03:46:26 GMT
|   Accept-Ranges: bytes
|   ETag: "20ba8ef391f8d31:0"
|   Server: Microsoft-IIS/7.5
|   X-Powered-By: ASP.NET
|   Date: Fri, 20 May 2022 19:45:35 GMT
|   Connection: close
|   
|_  (Request type: HEAD)
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=10.10.10.93
|     
|     Path: http://10.10.10.93:80/
|     Line number: 7
|     Comment: 
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|_        -->
|_http-csrf: Couldn't find any CSRF vulnerabilities.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri May 20 15:46:41 2022 -- 1 IP address (1 host up) scanned in 120.09 seconds

```
