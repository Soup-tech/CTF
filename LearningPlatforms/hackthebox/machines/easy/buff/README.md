# Buff

## Information Gathering
Buff<br>
10.10.10.198<br>

Software Versions:
- Apache 2.4.43
- OpenSSL 1.1.1g
- PHP 7.4.6

## Enumeration
Of course start with your nmap scan:
```bash
# Nmap 7.92 scan initiated Fri Feb 18 23:44:37 2022 as: nmap -p- -sC -sV -oN nmap/buff.nmap -Pn 10.10.10.198
Nmap scan report for 10.10.10.198
Host is up (0.028s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT     STATE SERVICE    VERSION
7680/tcp open  pando-pub?
8080/tcp open  http       Apache httpd 2.4.43 ((Win64) OpenSSL/1.1.1g PHP/7.4.6)
| http-open-proxy: Potentially OPEN proxy.
|_Methods supported:CONNECTION
|_http-server-header: Apache/2.4.43 (Win64) OpenSSL/1.1.1g PHP/7.4.6
|_http-title: mrb3ns Bro Hut

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Feb 18 23:48:33 2022 -- 1 IP address (1 host up) scanned in 236.19 seconds

```
There is a webserver on 8080 so I of course run my Nikto and directory busting scan's. There is also a odd "pando-pub" service on 7680. I'll see if I can pull header information from that.
Directory Busting:
```bash

```
Nikto Scan:
```bash

```


## Exploitation

## Privilege Escalation