```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/xml/_quick_tcp_nmap.xml" 10.10.10.134
```

[/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/_quick_tcp_nmap.txt](file:///home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.92 scan initiated Sat May 21 13:35:27 2022 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/_quick_tcp_nmap.txt -oX /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/xml/_quick_tcp_nmap.xml 10.10.10.134
Increasing send delay for 10.10.10.134 from 0 to 5 due to 23 out of 56 dropped probes since last increase.
Increasing send delay for 10.10.10.134 from 5 to 10 due to 21 out of 51 dropped probes since last increase.
adjust_timeouts2: packet supposedly had rtt of -166290 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -166290 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -166306 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -166306 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -199930 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -199930 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -211067 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -211067 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -207967 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -207967 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -226840 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -226840 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -198936 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -198936 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -223976 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -223976 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -222593 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -222593 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -173422 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -173422 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -185410 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -185410 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -195542 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -195542 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -192273 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -192273 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -365603 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -365603 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -194582 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -194582 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -212937 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -212937 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -214497 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -214497 microseconds.  Ignoring time.
Nmap scan report for 10.10.10.134
Host is up, received user-set (0.039s latency).
Scanned at 2022-05-21 13:35:27 EDT for 49s
Not shown: 996 closed tcp ports (reset)
PORT    STATE SERVICE      REASON          VERSION
22/tcp  open  ssh          syn-ack ttl 127 OpenSSH for_Windows_7.9 (protocol 2.0)
| ssh-hostkey: 
|   2048 3a:56:ae:75:3c:78:0e:c8:56:4d:cb:1c:22:bf:45:8a (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3bG3TRRwV6dlU1lPbviOW+3fBC7wab+KSQ0Gyhvf9Z1OxFh9v5e6GP4rt5Ss76ic1oAJPIDvQwGlKdeUEnjtEtQXB/78Ptw6IPPPPwF5dI1W4GvoGR4MV5Q6CPpJ6HLIJdvAcn3isTCZgoJT69xRK0ymPnqUqaB+/ptC4xvHmW9ptHdYjDOFLlwxg17e7Sy0CA67PW/nXu7+OKaIOx0lLn8QPEcyrYVCWAqVcUsgNNAjR4h1G7tYLVg3SGrbSmIcxlhSMexIFIVfR37LFlNIYc6Pa58lj2MSQLusIzRoQxaXO4YSp/dM1tk7CN2cKx1PTd9VVSDH+/Nq0HCXPiYh3
|   256 cc:2e:56:ab:19:97:d5:bb:03:fb:82:cd:63:da:68:01 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBF1Mau7cS9INLBOXVd4TXFX/02+0gYbMoFzIayeYeEOAcFQrAXa1nxhHjhfpHXWEj2u0Z/hfPBzOLBGi/ngFRUg=
|   256 93:5f:5d:aa:ca:9f:53:e7:f2:82:e6:64:a8:a3:a0:18 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB34X2ZgGpYNXYb+KLFENmf0P0iQ22Q0sjws2ATjFsiN
135/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
139/tcp open  netbios-ssn  syn-ack ttl 127 Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds syn-ack ttl 127 Windows Server 2016 Standard 14393 microsoft-ds
Aggressive OS guesses: Microsoft Windows Server 2016 build 10586 - 14393 (96%), Microsoft Windows Server 2016 (94%), Microsoft Windows 10 1507 (93%), Microsoft Windows 10 1507 - 1607 (93%), Microsoft Windows 10 1511 (93%), Microsoft Windows Server 2012 (93%), Microsoft Windows Server 2012 R2 (93%), Microsoft Windows Server 2012 R2 Update 1 (93%), Microsoft Windows 7, Windows Server 2012, or Windows 8.1 Update 1 (93%), Microsoft Windows Vista SP1 - SP2, Windows Server 2008 SP2, or Windows 7 (93%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=5/21%OT=22%CT=1%CU=35671%PV=Y%DS=2%DC=T%G=Y%TM=6289231
OS:0%P=x86_64-pc-linux-gnu)SEQ(SP=108%GCD=1%ISR=10C%CI=I%II=I%TS=A)SEQ(SP=1
OS:08%GCD=1%ISR=10C%CI=I%TS=A)OPS(O1=M505NW8ST11%O2=M505NW8ST11%O3=M505NW8N
OS:NT11%O4=M505NW8ST11%O5=M505NW8ST11%O6=M505ST11)WIN(W1=2000%W2=2000%W3=20
OS:00%W4=2000%W5=2000%W6=2000)ECN(R=Y%DF=Y%T=80%W=2000%O=M505NW8NNS%CC=Y%Q=
OS:)T1(R=Y%DF=Y%T=80%S=O%A=S+%F=AS%RD=0%Q=)T2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=A
OS:R%O=%RD=0%Q=)T3(R=Y%DF=Y%T=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=
OS:80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0
OS:%Q=)T6(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=Z
OS:%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G
OS:%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=80%CD=Z)

Uptime guess: 0.001 days (since Sat May 21 13:34:47 2022)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=264 (Good luck!)
IP ID Sequence Generation: Busy server or unknown class
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time: 
|   date: 2022-05-21T17:36:21
|_  start_date: 2022-05-21T17:35:15
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 50404/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 26941/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 62104/udp): CLEAN (Failed to receive data)
|   Check 4 (port 18741/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: Bastion
|   NetBIOS computer name: BASTION\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-05-21T19:36:24+02:00
|_clock-skew: mean: -39m45s, deviation: 1h09m14s, median: 12s

TRACEROUTE (using port 32772/tcp)
HOP RTT      ADDRESS
1   38.23 ms 10.10.14.1
2   39.64 ms 10.10.10.134

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat May 21 13:36:16 2022 -- 1 IP address (1 host up) scanned in 49.10 seconds

```
