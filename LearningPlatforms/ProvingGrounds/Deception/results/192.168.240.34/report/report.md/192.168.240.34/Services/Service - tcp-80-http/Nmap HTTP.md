```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp80/xml/tcp_80_http_nmap.xml" 192.168.240.34
```

[/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp80/tcp_80_http_nmap.txt](file:///home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.92 scan initiated Sun Apr 10 00:03:19 2022 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp80/tcp_80_http_nmap.txt -oX /home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp80/xml/tcp_80_http_nmap.xml 192.168.240.34
Nmap scan report for 192.168.240.34
Host is up, received user-set (0.051s latency).
Scanned at 2022-04-10 00:03:19 EDT for 29s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON         VERSION
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-errors: 
| Spidering limited to: maxpagecount=40; withinhost=192.168.240.34
|   Found the following error pages: 
|   
|   Error Code: 404
|_  	http://192.168.240.34:80/manual
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-grep: 
|   (1) http://192.168.240.34:80/manual: 
|     (1) ip: 
|_      + 192.168.240.34
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1
|     /icons/
|       png: 1
|   Longest directory structure:
|     Depth: 1
|     Dir: /icons/
|   Total files found (by extension):
|_    Other: 1; png: 1
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
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
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-config-backup: ERROR: Script execution failed (use -d to debug)
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.240.34
|     
|     Path: http://192.168.240.34:80/
|     Line number: 201
|     Comment: 
|         <!--      <div class="table_of_contents floating_element">
|                 <div class="section_header section_header_grey">
|                   TABLE OF CONTENTS
|                 </div>
|                 <div class="table_of_contents_item floating_element">
|                   <a href="#about">About</a>
|                 </div>
|                 <div class="table_of_contents_item floating_element">
|                   <a href="#changes">Changes</a>
|                 </div>
|                 <div class="table_of_contents_item floating_element">
|                   <a href="#scope">Scope</a>
|                 </div>
|                 <div class="table_of_contents_item floating_element">
|                   <a href="#files">Config files</a>
|                 </div>
|               </div>
|         -->
|     
|     Path: http://192.168.240.34:80/
|     Line number: 148
|     Comment: 
|         <!--API old 1 : 765D61D8 -->
|     
|     Path: http://192.168.240.34:80/
|     Line number: 67
|     Comment: 
|         <!--API old2 : 327DEB -->
|     
|     Path: http://192.168.240.34:80/
|     Line number: 319
|     Comment: 
|         <!--API new : 882CF99-->
|     
|     Path: http://192.168.240.34:80/
|     Line number: 4
|     Comment: 
|         <!--
|             Modified from the Debian original for Ubuntu
|             Last updated: 2016-11-16
|             API old0 : 5F4DCC3B5AA
|             See: https://launchpad.net/bugs/1288690
|            
|_          -->
|_http-mobileversion-checker: No mobile version detected.
|_http-feed: Couldn't find any feeds.
|_http-malware-host: Host appears to be clean
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
| http-php-version: Logo query returned unknown hash 575bc53daebc79be9f14268c431ccd19
|_Credits query returned unknown hash 575bc53daebc79be9f14268c431ccd19
|_http-date: Sun, 10 Apr 2022 04:03:31 GMT; +1s from local time.
| http-enum: 
|   /wordpress/: Blog
|   /phpmyadmin/: phpMyAdmin
|_  /wordpress/wp-login.php: Wordpress login page.
| http-vhosts: 
|_128 names had status 200
|_http-referer-checker: Couldn't find any cross-domain scripts.
| http-headers: 
|   Date: Sun, 10 Apr 2022 04:03:31 GMT
|   Server: Apache/2.4.29 (Ubuntu)
|   Last-Modified: Fri, 24 Jan 2020 19:13:07 GMT
|   ETag: "2b12-59ce78c323eb1"
|   Accept-Ranges: bytes
|   Content-Length: 11026
|   Vary: Accept-Encoding
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-chrono: Request times for /; avg: 273.09ms; min: 219.69ms; max: 310.53ms

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Apr 10 00:03:49 2022 -- 1 IP address (1 host up) scanned in 29.97 seconds

```
