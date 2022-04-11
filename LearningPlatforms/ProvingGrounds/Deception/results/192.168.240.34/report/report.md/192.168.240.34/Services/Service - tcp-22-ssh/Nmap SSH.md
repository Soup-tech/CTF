```bash
nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 192.168.240.34
```

[/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp22/tcp_22_ssh_nmap.txt](file:///home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp22/tcp_22_ssh_nmap.txt):

```
# Nmap 7.92 scan initiated Sun Apr 10 00:03:19 2022 as: nmap -vv --reason -Pn -T4 -sV -p 22 --script=banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods -oN /home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp22/tcp_22_ssh_nmap.txt -oX /home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/tcp22/xml/tcp_22_ssh_nmap.xml 192.168.240.34
Nmap scan report for 192.168.240.34
Host is up, received user-set (0.061s latency).
Scanned at 2022-04-10 00:03:19 EDT for 2s

PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
|_banner: SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3
| ssh2-enum-algos: 
|   kex_algorithms: (10)
|       curve25519-sha256
|       curve25519-sha256@libssh.org
|       ecdh-sha2-nistp256
|       ecdh-sha2-nistp384
|       ecdh-sha2-nistp521
|       diffie-hellman-group-exchange-sha256
|       diffie-hellman-group16-sha512
|       diffie-hellman-group18-sha512
|       diffie-hellman-group14-sha256
|       diffie-hellman-group14-sha1
|   server_host_key_algorithms: (5)
|       ssh-rsa
|       rsa-sha2-512
|       rsa-sha2-256
|       ecdsa-sha2-nistp256
|       ssh-ed25519
|   encryption_algorithms: (6)
|       chacha20-poly1305@openssh.com
|       aes128-ctr
|       aes192-ctr
|       aes256-ctr
|       aes128-gcm@openssh.com
|       aes256-gcm@openssh.com
|   mac_algorithms: (10)
|       umac-64-etm@openssh.com
|       umac-128-etm@openssh.com
|       hmac-sha2-256-etm@openssh.com
|       hmac-sha2-512-etm@openssh.com
|       hmac-sha1-etm@openssh.com
|       umac-64@openssh.com
|       umac-128@openssh.com
|       hmac-sha2-256
|       hmac-sha2-512
|       hmac-sha1
|   compression_algorithms: (2)
|       none
|_      zlib@openssh.com
| ssh-auth-methods: 
|   Supported authentication methods: 
|     publickey
|_    password
| ssh-hostkey: 
|   2048 9d:d0:98:da:0d:32:3d:0b:3f:42:4d:d7:93:4f:fd:60 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLSsGJtpg5KvawG56yanORlHOGP7anzFKXq8ZDjuBD20sWrHl6g0J1+w497SyvRnB6EDOBGrjqlEXqlI7DvgrAo08GOCvoajuPpitLuC2rCfRC3b3ctn/n2+zGkkfsD5Y0U6PQrchRNpMKH/4nsaBcrTV8ZkEGF+VNYhnTO7c1vGhpH0i5c7UzyKvfqz/KzH4YryUpC1opxB9pn0jHH+iQ8H+Brne/bvOmpyvoy84CzuunshxMmAV9qdaLmZxOOF25SF5uHh6r1h8tVG8yLbD1N7IfPXXy0GpZZZIBt4i/ZQVpfk1i0GsY4/mL3VCrtFsO4p2PxRLVws5Fpces+pDN
|   256 4c:f4:2e:24:82:cf:9c:8d:e2:0c:52:4b:2e:a5:12:d9 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDwKM2aO1LW/C4gfLHyFmkrfcPcXVHvIEK8JN9pk/9kNhZKz8X9byyxiWMnNS/6AQNMAV0d5B+d0/VK2eps90ZI=
|   256 a9:fb:e3:f4:ba:d6:1e:72:e7:97:25:82:87:6e:ea:01 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEOULyvRe2blVRaHM9twRKyE34SQUyGPMjVmRv2srgvv
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Apr 10 00:03:21 2022 -- 1 IP address (1 host up) scanned in 2.40 seconds

```
