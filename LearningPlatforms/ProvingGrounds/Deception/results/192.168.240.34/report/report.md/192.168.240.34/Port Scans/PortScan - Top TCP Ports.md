```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/xml/_quick_tcp_nmap.xml" 192.168.240.34
```

[/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/_quick_tcp_nmap.txt](file:///home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.92 scan initiated Sun Apr 10 00:03:03 2022 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/_quick_tcp_nmap.txt -oX /home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/xml/_quick_tcp_nmap.xml 192.168.240.34
Nmap scan report for 192.168.240.34
Host is up, received user-set (0.051s latency).
Scanned at 2022-04-10 00:03:03 EDT for 15s
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9d:d0:98:da:0d:32:3d:0b:3f:42:4d:d7:93:4f:fd:60 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLSsGJtpg5KvawG56yanORlHOGP7anzFKXq8ZDjuBD20sWrHl6g0J1+w497SyvRnB6EDOBGrjqlEXqlI7DvgrAo08GOCvoajuPpitLuC2rCfRC3b3ctn/n2+zGkkfsD5Y0U6PQrchRNpMKH/4nsaBcrTV8ZkEGF+VNYhnTO7c1vGhpH0i5c7UzyKvfqz/KzH4YryUpC1opxB9pn0jHH+iQ8H+Brne/bvOmpyvoy84CzuunshxMmAV9qdaLmZxOOF25SF5uHh6r1h8tVG8yLbD1N7IfPXXy0GpZZZIBt4i/ZQVpfk1i0GsY4/mL3VCrtFsO4p2PxRLVws5Fpces+pDN
|   256 4c:f4:2e:24:82:cf:9c:8d:e2:0c:52:4b:2e:a5:12:d9 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDwKM2aO1LW/C4gfLHyFmkrfcPcXVHvIEK8JN9pk/9kNhZKz8X9byyxiWMnNS/6AQNMAV0d5B+d0/VK2eps90ZI=
|   256 a9:fb:e3:f4:ba:d6:1e:72:e7:97:25:82:87:6e:ea:01 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEOULyvRe2blVRaHM9twRKyE34SQUyGPMjVmRv2srgvv
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: Apache2 Ubuntu Default Page: It works
OS fingerprint not ideal because: Didn't receive UDP response. Please try again with -sSU
No OS matches for host
TCP/IP fingerprint:
SCAN(V=7.92%E=4%D=4/10%OT=22%CT=1%CU=%PV=Y%DS=2%DC=T%G=N%TM=62525706%P=x86_64-pc-linux-gnu)
SEQ(SP=101%GCD=1%ISR=107%TI=Z%TS=A)
OPS(O1=M54EST11NW7%O2=M54EST11NW7%O3=M54ENNT11NW7%O4=M54EST11NW7%O5=M54EST11NW7%O6=M54EST11)
WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)
ECN(R=N)
T1(R=Y%DF=Y%TG=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=N)
T5(R=N)
T6(R=N)
T7(R=N)
U1(R=N)
IE(R=Y%DFI=N%TG=40%CD=S)

Uptime guess: 25.759 days (since Tue Mar 15 05:50:04 2022)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=257 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 3306/tcp)
HOP RTT      ADDRESS
1   50.25 ms 192.168.49.1
2   50.22 ms 192.168.240.34

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Apr 10 00:03:18 2022 -- 1 IP address (1 host up) scanned in 15.67 seconds

```
