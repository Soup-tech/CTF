# Blue

## Information Gathering
Blue<br>
10.10.10.40<br>

## Enumeration
Start with an nmap scan:
```bash
# Nmap 7.92 scan initiated Mon Feb 14 00:25:49 2022 as: nmap -sC -sV -oN nmap/blue.nmap -Pn 10.10.10.40
Nmap scan report for 10.10.10.40
Host is up (0.028s latency).
Not shown: 991 closed tcp ports (reset)
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49155/tcp open  msrpc        Microsoft Windows RPC
49156/tcp open  msrpc        Microsoft Windows RPC
49157/tcp open  msrpc        Microsoft Windows RPC
Service Info: Host: HARIS-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   2.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-02-14T05:33:56
|_  start_date: 2022-02-14T05:32:46
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: haris-PC
|   NetBIOS computer name: HARIS-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-02-14T05:33:57+00:00
|_clock-skew: mean: 7m01s, deviation: 1s, median: 7m00s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Feb 14 00:27:02 2022 -- 1 IP address (1 host up) scanned in 72.88 seconds
```
Because we have SMB running on this Windows machine, I also ran a enum4linux script but nothing was returned. I also ran an exploitation scanner since RPC and SMB were running.
```bash
# Nmap 7.92 scan initiated Mon Feb 14 00:30:02 2022 as: nmap -p135,139,445 --script vuln -Pn -oN nmap/vuln_scanner.nmap 10.10.10.40
Nmap scan report for 10.10.10.40
Host is up (0.027s latency).

PORT    STATE SERVICE
135/tcp open  msrpc
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Host script results:
|_smb-vuln-ms10-054: false
|_smb-vuln-ms10-061: NT_STATUS_OBJECT_NAME_NOT_FOUND
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143

# Nmap done at Mon Feb 14 00:30:28 2022 -- 1 IP address (1 host up) scanned in 26.68 seconds

```
## Exploitation
Just looking at the vulnerability scan from nmap shows ms17-010 which is EternalBlue. Booting Metasploit and using windows/smb/ms17_010_eternalblue will drop you right into a NT AUTHORITY\SYSTEM shell.