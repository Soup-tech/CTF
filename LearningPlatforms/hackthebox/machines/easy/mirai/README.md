# Mirai

## Information Gathering
10.10.10.48<br>
Mirai<br>

<ul>Software Version
	<li>OpenSSH 6.7p1</li>
	<li>dnsmasq-2.76</li>
	<li>lighttpd 1.4.35</li>
	<li>Pi-hole v3.1.4</li>
	<li>Platinum UPnP 1.0.5.13</li>
</ul>

## Enumeration
Start with an nmap scan:
```bash
# Nmap 7.92 scan initiated Wed Feb 16 17:59:50 2022 as: nmap -p- -A -oN nmap/all_ports.nmap 10.10.10.48
Nmap scan report for 10.10.10.48
Host is up (0.027s latency).
Not shown: 65529 closed tcp ports (reset)
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 6.7p1 Debian 5+deb8u3 (protocol 2.0)
| ssh-hostkey: 
|   1024 aa:ef:5c:e0:8e:86:97:82:47:ff:4a:e5:40:18:90:c5 (DSA)
|   2048 e8:c1:9d:c5:43:ab:fe:61:23:3b:d7:e4:af:9b:74:18 (RSA)
|   256 b6:a0:78:38:d0:c8:10:94:8b:44:b2:ea:a0:17:42:2b (ECDSA)
|_  256 4d:68:40:f7:20:c4:e5:52:80:7a:44:38:b8:a2:a7:52 (ED25519)
53/tcp    open  domain  dnsmasq 2.76
| dns-nsid: 
|_  bind.version: dnsmasq-2.76
80/tcp    open  http    lighttpd 1.4.35
|_http-title: Site doesnt have a title (text/html; charset=UTF-8).
|_http-server-header: lighttpd/1.4.35
1326/tcp  open  upnp    Platinum UPnP 1.0.5.13 (UPnP/1.0 DLNADOC/1.50)
32400/tcp open  http    Plex Media Server httpd
|_http-title: Unauthorized
|_http-favicon: Plex
|_http-cors: HEAD GET POST PUT DELETE OPTIONS
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Server returned status 401 but no WWW-Authenticate header.
32469/tcp open  upnp    Platinum UPnP 1.0.5.13 (UPnP/1.0 DLNADOC/1.50)
Aggressive OS guesses: Linux 3.12 (95%), Linux 3.13 (95%), Linux 3.16 (95%), Linux 3.18 (95%), Linux 3.2 - 4.9 (95%), Linux 3.8 - 3.11 (95%), Linux 4.8 (95%), Linux 4.4 (95%), Linux 4.2 (95%), ASUS RT-N56U WAP (Linux 3.4) (95%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 3306/tcp)
HOP RTT      ADDRESS
1   26.97 ms 10.10.14.1
2   27.02 ms 10.10.10.48

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Feb 16 18:04:01 2022 -- 1 IP address (1 host up) scanned in 251.32 seconds

```
There are two webservers so I have to do twice the amount of enumeration.
For port 80 the directory busting:
```bash
/admin                (Status: 301) [Size: 0] [--> http://10.10.10.48/admin/]
/versions             (Status: 200) [Size: 18]
```
And the nikto scan:
```bash
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.48
+ Target Port: 80
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET Uncommon header 'x-pi-hole' found, with contents: A black hole for Internet advertisements.
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ OPTIONS Allowed HTTP Methods: OPTIONS, GET, HEAD, POST 
```
And for port 32400 the directory scanning:
```bash
/img                  (Status: 200) [Size: 0]
/index.html           (Status: 200) [Size: 4223]
/common               (Status: 200) [Size: 0]
/desktop              (Status: 200) [Size: 0]
/js                   (Status: 200) [Size: 0]
/setup.html           (Status: 200) [Size: 752]
/translations         (Status: 200) [Size: 0]
/swf                  (Status: 200) [Size: 0]
```
And the nikto scan
```bash
- Nikto v2.1.6/2.1.5
+ No web server found on 10.10.10.48:324400
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.48
+ Target Port: 32400
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET Uncommon header 'x-plex-protocol' found, with contents: 1.0
+ GET The site uses SSL and the Strict-Transport-Security HTTP header is not defined.
+ GET The site uses SSL and Expect-CT header is not present.
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ GET /clientaccesspolicy.xml contains a full wildcard entry. See http://msdn.microsoft.com/en-us/library/cc197955(v=vs.95).aspx
+ GET /clientaccesspolicy.xml contains 12 lines which should be manually viewed for improper domains or wildcards.
+ GET /crossdomain.xml contains a full wildcard entry. See http://jeremiahgrossman.blogspot.com/2008/05/crossdomainxml-invites-cross-site.html
+ GET Uncommon header 'x-plex-content-original-length' found, with contents: 193
+ GET Uncommon header 'x-plex-content-compressed-length' found, with contents: 157
+ GET The Content-Encoding header is set to "deflate" this may mean that the server is vulnerable to the BREACH attack.
+ OSVDB-39272: GET /favicon.ico file identifies this app/server as: Plex Media Server
+ GET Server is using a wildcard certificate: *.78063b2b367a4a389895262d75b0b03c.plex.direct
+ GET Hostname '10.10.10.48' does not match certificates names: *.78063b2b367a4a389895262d75b0b03c.plex.direct
+ GET Retrieved access-control-allow-origin header: *
+ GET /webmail/: Web based mail package installed.

```

## Exploitation
After many failed exploitation attempts for both webservers, I thought about the name of the box: Mirai. Mirai was a famous botnet which exploited default credentials in IoT devices. I figure that this machine must be a raspberry-pi because there is a pi-hole running. SSH'ing into the server as "pi" and using "raspberry" as the credentials yields a foothold.

## Privilege Escalation
There is no privilege escalation for this box as the user "pi" is able to run any command sudo root privileges. However, you must obtain the root flag in an unconventional way. When looking at root.txt, there is a message
```
I lost my original root.txt! I think I may have a backup on my USB stick...
```
Listing all mounts:
```bash
df 

Filesystem     1K-blocks    Used Available Use% Mounted on
aufs             8856504 2833540   5550032  34% /
tmpfs             102396    4868     97528   5% /run
/dev/sda1        1354528 1354528         0 100% /lib/live/mount/persistence/sda1
/dev/loop0       1267456 1267456         0 100% /lib/live/mount/rootfs/filesystem.squashfs
tmpfs             255988       0    255988   0% /lib/live/mount/overlay
/dev/sda2        8856504 2833540   5550032  34% /lib/live/mount/persistence/sda2
devtmpfs           10240       0     10240   0% /dev
tmpfs             255988       8    255980   1% /dev/shm
tmpfs               5120       4      5116   1% /run/lock
tmpfs             255988       0    255988   0% /sys/fs/cgroup
tmpfs             255988       8    255980   1% /tmp
/dev/sdb            8887      93      8078   2% /media/usbstick
tmpfs              51200       0     51200   0% /run/user/999
tmpfs              51200       0     51200   0% /run/user/1000
```
There is a /media/usbstick mounted on /dev/sdb. When navigating to this directory, there is another note damnit.txt:
```
Damnit! Sorry man I accidentally deleted your files off the USB stick.
Do you know if there is any way to get them back?

-James
```
A simple way to obtain the flag is:
```bash
strings /dev/sdb

>r &
/media/usbstick
lost+found
root.txt
damnit.txt
>r &
>r &
/media/usbstick
lost+found
root.txt
damnit.txt
>r &
/media/usbstick
2]8^
lost+found
root.txt
damnit.txt
>r &
3d3e483143ff12ec505d026fa13e020b
Damnit! Sorry man I accidentally deleted your files off the USB stick.
Do you know if there is any way to get them back?
-James
```