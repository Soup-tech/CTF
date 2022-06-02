```bash
whatweb --color=never --no-errors -a 3 -v http://10.10.10.134:47001 2>&1
```

[/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp47001/tcp_47001_http_whatweb.txt](file:///home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp47001/tcp_47001_http_whatweb.txt):

```
WhatWeb report for http://10.10.10.134:47001
Status    : 404 Not Found
Title     : Not Found
IP        : 10.10.10.134
Country   : RESERVED, ZZ

Summary   : HTTPServer[Microsoft-HTTPAPI/2.0], Microsoft-HTTPAPI[2.0]

Detected Plugins:
[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	String       : Microsoft-HTTPAPI/2.0 (from server string)

[ Microsoft-HTTPAPI ]
	The HTTP Server API enables applications to communicate
	over HTTP without using Microsoft Internet Information
	Server (IIS). Applications can register to receive HTTP
	requests for particular URLs, receive HTTP requests, and
	send HTTP responses. The HTTP Server API includes SSL
	support so that applications can exchange data over secure
	HTTP connections without IIS. It is also designed to work
	with I/O completion ports.

	Version      : 2.0
	Website     : http://msdn.microsoft.com/en-us/library/aa364510%28v=vs.85%29.aspx

HTTP Headers:
	HTTP/1.1 404 Not Found
	Content-Type: text/html; charset=us-ascii
	Server: Microsoft-HTTPAPI/2.0
	Date: Sat, 21 May 2022 17:44:17 GMT
	Connection: close
	Content-Length: 315



```
