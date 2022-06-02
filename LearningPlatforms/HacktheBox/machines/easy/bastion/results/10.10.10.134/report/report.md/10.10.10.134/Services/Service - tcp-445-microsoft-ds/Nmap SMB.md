```bash
nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.10.134
```

[/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp445/tcp_445_smb_nmap.txt](file:///home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp445/tcp_445_smb_nmap.txt):

```
# Nmap 7.92 scan initiated Sat May 21 13:36:16 2022 as: nmap -vv --reason -Pn -T4 -sV -p 445 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp445/tcp_445_smb_nmap.txt -oX /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp445/xml/tcp_445_smb_nmap.xml 10.10.10.134
Nmap scan report for 10.10.10.134
Host is up, received user-set (0.040s latency).
Scanned at 2022-05-21 13:36:17 EDT for 86s

PORT    STATE SERVICE      REASON          VERSION
445/tcp open  microsoft-ds syn-ack ttl 127 Windows Server 2016 Standard 14393 microsoft-ds
Service Info: OS: Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-protocols: 
|   dialects: 
|     NT LM 0.12 (SMBv1) [dangerous, but default]
|     2.0.2
|     2.1
|     3.0
|     3.0.2
|_    3.1.1
| smb2-capabilities: 
|   2.0.2: 
|     Distributed File System
|   2.1: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3.0: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3.0.2: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3.1.1: 
|     Distributed File System
|     Leasing
|_    Multi-credit operations
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: Bastion
|   NetBIOS computer name: BASTION\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-05-21T19:36:57+02:00
| smb-mbenum: 
|_  ERROR: Call to Browser Service failed with status = 2184
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time: 
|   date: 2022-05-21T17:36:56
|_  start_date: 2022-05-21T17:35:15
|_smb-vuln-ms10-061: ERROR: Script execution failed (use -d to debug)
|_smb-system-info: ERROR: Script execution failed (use -d to debug)
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
|_smb-print-text: false
| smb-enum-sessions: 
|_  <nobody>

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat May 21 13:37:43 2022 -- 1 IP address (1 host up) scanned in 86.58 seconds

```
