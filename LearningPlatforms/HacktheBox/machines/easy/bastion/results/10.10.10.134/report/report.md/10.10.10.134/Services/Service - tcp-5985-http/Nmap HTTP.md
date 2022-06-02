```bash
nmap -vv --reason -Pn -T4 -sV -p 5985 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/xml/tcp_5985_http_nmap.xml" 10.10.10.134
```

[/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_nmap.txt](file:///home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_nmap.txt):

```
# Nmap 7.92 scan initiated Sat May 21 13:44:03 2022 as: nmap -vv --reason -Pn -T4 -sV -p 5985 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_nmap.txt -oX /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/xml/tcp_5985_http_nmap.xml 10.10.10.134
Nmap scan report for 10.10.10.134
Host is up, received user-set (0.039s latency).
Scanned at 2022-05-21 13:44:04 EDT for 243s

Bug in http-security-headers: no string output.
PORT     STATE SERVICE REASON          VERSION
5985/tcp open  http    syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
| http-useragent-tester: 
|   Status for browser useragent: 404
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
|_http-malware-host: Host appears to be clean
|_http-mobileversion-checker: No mobile version detected.
|_http-comments-displayer: Couldn't find any comments.
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-config-backup: ERROR: Script execution failed (use -d to debug)
|_http-title: Not Found
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
| http-vhosts: 
|_128 names had status 404
|_http-date: Sat, 21 May 2022 17:44:26 GMT; +13s from local time.
|_http-feed: Couldn't find any feeds.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-sitemap-generator: 
|   Directory structure:
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-chrono: Request times for /; avg: 152.55ms; min: 151.40ms; max: 153.18ms
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-referer-checker: Couldn't find any cross-domain scripts.
| http-headers: 
|   Content-Type: text/html; charset=us-ascii
|   Server: Microsoft-HTTPAPI/2.0
|   Date: Sat, 21 May 2022 17:44:30 GMT
|   Connection: close
|   Content-Length: 315
|   
|_  (Request type: GET)
| http-errors: 
| Spidering limited to: maxpagecount=40; withinhost=10.10.10.134
|   Found the following error pages: 
|   
|   Error Code: 404
|_  	http://10.10.10.134:5985/
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat May 21 13:48:07 2022 -- 1 IP address (1 host up) scanned in 244.07 seconds

```
