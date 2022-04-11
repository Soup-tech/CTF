```bash
whatweb --color=never --no-errors -a 3 -v http://192.168.240.34:80 2>&1
```

[/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp80/tcp_80_http_whatweb.txt](file:///home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp80/tcp_80_http_whatweb.txt):

```
WhatWeb report for http://192.168.240.34:80
Status    : 200 OK
Title     : Apache2 Ubuntu Default Page: It works
IP        : 192.168.240.34
Country   : RESERVED, ZZ

Summary   : HTTPServer[Ubuntu Linux][Apache/2.4.29 (Ubuntu)], Apache[2.4.29]

Detected Plugins:
[ Apache ]
	The Apache HTTP Server Project is an effort to develop and
	maintain an open-source HTTP server for modern operating
	systems including UNIX and Windows NT. The goal of this
	project is to provide a secure, efficient and extensible
	server that provides HTTP services in sync with the current
	HTTP standards.

	Version      : 2.4.29 (from HTTP Server Header)
	Google Dorks: (3)
	Website     : http://httpd.apache.org/

[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	OS           : Ubuntu Linux
	String       : Apache/2.4.29 (Ubuntu) (from server string)

HTTP Headers:
	HTTP/1.1 200 OK
	Date: Sun, 10 Apr 2022 04:03:25 GMT
	Server: Apache/2.4.29 (Ubuntu)
	Last-Modified: Fri, 24 Jan 2020 19:13:07 GMT
	ETag: "2b12-59ce78c323eb1-gzip"
	Accept-Ranges: bytes
	Vary: Accept-Encoding
	Content-Encoding: gzip
	Content-Length: 3232
	Connection: close
	Content-Type: text/html



```
