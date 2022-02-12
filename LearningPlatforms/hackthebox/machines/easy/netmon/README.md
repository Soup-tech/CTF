# Netmon

## Information Gathering

### Initial
10.10.10.152
Netmon

## Enumeration and Scanning
Nmap scan(s).
First my safe nmap scan
```bash
# Nmap 7.92 scan initiated Mon Jan 17 19:53:25 2022 as: nmap -sC -sV -oN nmap/netmon_safe.nmap -Pn 10.10.10.152
Nmap scan report for 10.10.10.152
Host is up (0.028s latency).
Not shown: 995 closed tcp ports (reset)
PORT    STATE SERVICE      VERSION
21/tcp  open  ftp          Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| 02-02-19  11:18PM                 1024 .rnd
| 02-25-19  09:15PM       <DIR>          inetpub
| 07-16-16  08:18AM       <DIR>          PerfLogs
| 02-25-19  09:56PM       <DIR>          Program Files
| 02-02-19  11:28PM       <DIR>          Program Files (x86)
| 02-03-19  07:08AM       <DIR>          Users
|_02-25-19  10:49PM       <DIR>          Windows
80/tcp  open  http         Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)
|_http-trane-info: Problem with XML parsing of /evox/about
| http-title: Welcome | PRTG Network Monitor (NETMON)
|_Requested resource was /index.htm
|_http-server-header: PRTG/18.1.37.13946
135/tcp open  msrpc        Microsoft Windows RPC
139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-01-18T01:08:39
|_  start_date: 2022-01-18T01:06:53
|_clock-skew: mean: 15m02s, deviation: 0s, median: 15m01s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 17 19:53:41 2022 -- 1 IP address (1 host up) scanned in 16.52 seconds

```
Then my aggressive scan
```bash
# Nmap 7.92 scan initiated Mon Jan 17 19:58:05 2022 as: nmap -p- -A -O -oN nmap/netmon_aggressive.nmap 10.10.10.152
Nmap scan report for 10.10.10.152
Host is up (0.028s latency).
Not shown: 65522 closed tcp ports (reset)
PORT      STATE SERVICE      VERSION
21/tcp    open  ftp          Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| 02-02-19  11:18PM                 1024 .rnd
| 02-25-19  09:15PM       <DIR>          inetpub
| 07-16-16  08:18AM       <DIR>          PerfLogs
| 02-25-19  09:56PM       <DIR>          Program Files
| 02-02-19  11:28PM       <DIR>          Program Files (x86)
| 02-03-19  07:08AM       <DIR>          Users
|_02-25-19  10:49PM       <DIR>          Windows
80/tcp    open  http         Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)
|_http-server-header: PRTG/18.1.37.13946
|_http-trane-info: Problem with XML parsing of /evox/about
| http-title: Welcome | PRTG Network Monitor (NETMON)
|_Requested resource was /index.htm
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
5985/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
47001/tcp open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc        Microsoft Windows RPC
49665/tcp open  msrpc        Microsoft Windows RPC
49666/tcp open  msrpc        Microsoft Windows RPC
49667/tcp open  msrpc        Microsoft Windows RPC
49668/tcp open  msrpc        Microsoft Windows RPC
49669/tcp open  msrpc        Microsoft Windows RPC
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=1/17%OT=21%CT=1%CU=42014%PV=Y%DS=2%DC=T%G=Y%TM=61E6112
OS:1%P=x86_64-pc-linux-gnu)SEQ(SP=108%GCD=1%ISR=109%TI=I%CI=I%II=I%SS=S%TS=
OS:A)OPS(O1=M505NW8ST11%O2=M505NW8ST11%O3=M505NW8NNT11%O4=M505NW8ST11%O5=M5
OS:05NW8ST11%O6=M505ST11)WIN(W1=2000%W2=2000%W3=2000%W4=2000%W5=2000%W6=200
OS:0)ECN(R=Y%DF=Y%T=80%W=2000%O=M505NW8NNS%CC=Y%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S
OS:+%F=AS%RD=0%Q=)T2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)T3(R=Y%DF=Y%
OS:T=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=
OS:0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=80%W=0%
OS:S=A%A=O%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(
OS:R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=
OS:N%T=80%CD=Z)

Network Distance: 2 hops
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time: 
|   date: 2022-01-18T01:15:15
|_  start_date: 2022-01-18T01:06:53
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
|_clock-skew: mean: 15m02s, deviation: 0s, median: 15m01s

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   27.52 ms 10.10.14.1
2   27.56 ms 10.10.10.152

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 17 20:00:17 2022 -- 1 IP address (1 host up) scanned in 132.89 seconds
```

On port 80, Nikto.
Nikto<br>
```bash
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.152
+ Target Port: 80
+ GET The anti-clickjacking X-Frame-Options header is not present.
```

## Exploitation

### General Observations
- Indy httpd 18.1.37.13946 (Paessler PRTG Bandwidth Monitor) - May be vulnerable to <a href="https://www.exploit-db.com/exploits/46527">RCE</a>
- There is Anonymous login allowed in FTP.
- There is a WinRM server on port 5985, 47001, getting credentials may lead to a remote login using evil-winrm

### FTP
I start by copying the entire contents of the FTP server. This seems to be everything on the server. The only thing I don't have access to is the Administrator directory.
```bash
wget -r ftp://Anonymous:Anonymous@10.10.10.152/
```
I have access to all the PRTG files. I first start looking for any file that may hold credentials. I tried .db, .txt files, and .dat files. No luck. I began scanning the entire copied drive looking for old or backup files that may store credentials. Anything with a .bak or .old
```bash
find . -name *.bak -type f
./ProgramData/Paessler/PRTG Network Monitor/PRTG Configuration.old.bak
./Users/All Users/Paessler/PRTG Network Monitor/PRTG Configuration.old.bak

```
I got two hits of what appear to be the same file. Going through the file shows cleartext credentials <b>prtgadmin:PrTg@dmin2018</b>. However, after trying these credentials it did not work. Considering this file is a .bak, I may just need to update the year. Thus the real credentials were <b>prtgadmin:PrTg@dmin2019</b>.<br>
The previously stated RCE actually has a Metasploit module: <b>windows/http/prtg_authenticated_rce</b>. Loading this up with the proper options and exploiting gets me Administrator.
