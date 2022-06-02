# Legacy

## Information Gathering
10.10.10.4<br>
Legacy<br>

## Enumeration
Start with a basic nmap scan:<br>
```bash
# Nmap 7.92 scan initiated Sun Feb 13 19:03:27 2022 as: nmap -sC -sV -oN nmap/legacy.nmap 10.10.10.4
Nmap scan report for 10.10.10.4
Host is up (0.028s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT     STATE  SERVICE       VERSION
139/tcp  open   netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open   microsoft-ds  Windows XP microsoft-ds
3389/tcp closed ms-wbt-server
Service Info: OSs: Windows, Windows XP; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_xp

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
|_clock-skew: mean: 5d01h04m36s, deviation: 1h24m50s, median: 5d00h04m36s
|_nbstat: NetBIOS name: LEGACY, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:b9:48:ad (VMware)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows XP (Windows 2000 LAN Manager)
|   OS CPE: cpe:/o:microsoft:windows_xp::-
|   Computer name: legacy
|   NetBIOS computer name: LEGACY\x00
|   Workgroup: HTB\x00
|_  System time: 2022-02-19T04:08:17+02:00

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Feb 13 19:04:20 2022 -- 1 IP address (1 host up) scanned in 53.68 seconds
```
There's not a lot here. I try enum4linux but I don't get a whole lot:
```bash
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Sun Feb 13 19:13:20 2022

 ========================== 
|    Target Information    |
 ========================== 
Target ........... 10.10.10.4
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ================================================== 
|    Enumerating Workgroup/Domain on 10.10.10.4    |
 ================================================== 
[E] Cant find workgroup/domain


 ========================================== 
|    Nbtstat Information for 10.10.10.4    |
 ========================================== 
Looking up status of 10.10.10.4
No reply from 10.10.10.4

 =================================== 
|    Session Check on 10.10.10.4    |
 =================================== 
[E] Server doesnt allow session using username '', password ''.  Aborting remainder of tests.

```
With the lack of ports and that only 139 and 445 are open, I begin vulnerability scanning both these ports with nmap.
```bash
# Nmap 7.92 scan initiated Sun Feb 13 19:16:29 2022 as: nmap -p139,445 --script vuln -Pn -oN nmap/smb_vuln_report.nmap 10.10.10.4
Nmap scan report for 10.10.10.4
Host is up (0.027s latency).

PORT    STATE SERVICE
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Host script results:
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED
| smb-vuln-ms08-067: 
|   VULNERABLE:
|   Microsoft Windows system vulnerable to remote code execution (MS08-067)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2008-4250
|           The Server service in Microsoft Windows 2000 SP4, XP SP2 and SP3, Server 2003 SP1 and SP2,
|           Vista Gold and SP1, Server 2008, and 7 Pre-Beta allows remote attackers to execute arbitrary
|           code via a crafted RPC request that triggers the overflow during path canonicalization.
|           
|     Disclosure date: 2008-10-23
|     References:
|       https://technet.microsoft.com/en-us/library/security/ms08-067.aspx
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-4250
|_smb-vuln-ms10-061: ERROR: Script execution failed (use -d to debug)
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
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|_      https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|_smb-vuln-ms10-054: false

# Nmap done at Sun Feb 13 19:16:54 2022 -- 1 IP address (1 host up) scanned in 24.75 seconds

```
I get back two hits. Ms17-010 is eternalblue but I decide to use the first one.

## Exploitation
Spinning up Metasploit I search for ms08-067. Only one result comes back. I fill in the options and the exploit runs. This drops me right into a NT AUTHORITY\SYSTEM shell. 
