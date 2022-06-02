```bash
nmap -vv --reason -Pn -T4 -sV -p 49668 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49668/tcp_49668_rpc_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49668/xml/tcp_49668_rpc_nmap.xml" 10.10.10.134
```

[/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49668/tcp_49668_rpc_nmap.txt](file:///home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49668/tcp_49668_rpc_nmap.txt):

```
# Nmap 7.92 scan initiated Sat May 21 13:44:03 2022 as: nmap -vv --reason -Pn -T4 -sV -p 49668 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49668/tcp_49668_rpc_nmap.txt -oX /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49668/xml/tcp_49668_rpc_nmap.xml 10.10.10.134
Nmap scan report for 10.10.10.134
Host is up, received user-set (0.043s latency).
Scanned at 2022-05-21 13:44:04 EDT for 69s

PORT      STATE SERVICE REASON          VERSION
49668/tcp open  msrpc   syn-ack ttl 127 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat May 21 13:45:13 2022 -- 1 IP address (1 host up) scanned in 69.83 seconds

```
