```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/xml/_quick_tcp_nmap.xml" 10.10.10.134

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/_full_tcp_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/xml/_full_tcp_nmap.xml" 10.10.10.134

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/xml/_top_100_udp_nmap.xml" 10.10.10.134

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/xml/_quick_tcp_nmap.xml" 10.10.10.134

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/_full_tcp_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/xml/_full_tcp_nmap.xml" 10.10.10.134

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/xml/_top_100_udp_nmap.xml" 10.10.10.134

nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 10.10.10.134

getArch.py -target 10.10.10.134

nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 10.10.10.134

impacket-rpcdump -port 135 10.10.10.134

enum4linux -a -M -l -d 10.10.10.134 2>&1

nbtscan -rvh 10.10.10.134 2>&1

nmap -vv --reason -Pn -T4 -sV -p 139 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp139/tcp_139_smb_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp139/xml/tcp_139_smb_nmap.xml" 10.10.10.134

smbclient -L //10.10.10.134 -N -I 10.10.10.134 2>&1

smbmap -H 10.10.10.134 -P 139 2>&1

nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.10.134

smbmap -H 10.10.10.134 -P 445 2>&1

smbmap -u null -p "" -H 10.10.10.134 -P 445 2>&1

smbmap -H 10.10.10.134 -P 445 -R 2>&1

smbmap -u null -p "" -H 10.10.10.134 -P 445 -R 2>&1

smbmap -u null -p "" -H 10.10.10.134 -P 139 2>&1

smbmap -H 10.10.10.134 -P 445 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 10.10.10.134 -P 445 -x "ipconfig /all" 2>&1

smbmap -H 10.10.10.134 -P 139 -R 2>&1

smbmap -u null -p "" -H 10.10.10.134 -P 139 -R 2>&1

smbmap -H 10.10.10.134 -P 139 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 10.10.10.134 -P 139 -x "ipconfig /all" 2>&1

feroxbuster -u http://10.10.10.134:5985/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_feroxbuster_dirbuster.txt"

curl -sSik http://10.10.10.134:5985/

curl -sSikf http://10.10.10.134:5985/.well-known/security.txt

curl -sSikf http://10.10.10.134:5985/robots.txt

nmap -vv --reason -Pn -T4 -sV -p 5985 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/xml/tcp_5985_http_nmap.xml" 10.10.10.134

whatweb --color=never --no-errors -a 3 -v http://10.10.10.134:5985 2>&1

wkhtmltoimage --format png http://10.10.10.134:5985/ /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_screenshot.png

feroxbuster -u http://10.10.10.134:47001/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp47001/tcp_47001_http_feroxbuster_dirbuster.txt"

curl -sSik http://10.10.10.134:47001/

curl -sSikf http://10.10.10.134:47001/.well-known/security.txt

curl -sSikf http://10.10.10.134:47001/robots.txt

nmap -vv --reason -Pn -T4 -sV -p 47001 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp47001/tcp_47001_http_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp47001/xml/tcp_47001_http_nmap.xml" 10.10.10.134

whatweb --color=never --no-errors -a 3 -v http://10.10.10.134:47001 2>&1

wkhtmltoimage --format png http://10.10.10.134:47001/ /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp47001/tcp_47001_http_screenshot.png

nmap -vv --reason -Pn -T4 -sV -p 49664 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49664/tcp_49664_rpc_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49664/xml/tcp_49664_rpc_nmap.xml" 10.10.10.134

nmap -vv --reason -Pn -T4 -sV -p 49665 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49665/tcp_49665_rpc_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49665/xml/tcp_49665_rpc_nmap.xml" 10.10.10.134

nmap -vv --reason -Pn -T4 -sV -p 49666 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49666/tcp_49666_rpc_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49666/xml/tcp_49666_rpc_nmap.xml" 10.10.10.134

nmap -vv --reason -Pn -T4 -sV -p 49667 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49667/tcp_49667_rpc_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49667/xml/tcp_49667_rpc_nmap.xml" 10.10.10.134

nmap -vv --reason -Pn -T4 -sV -p 49668 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49668/tcp_49668_rpc_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49668/xml/tcp_49668_rpc_nmap.xml" 10.10.10.134

nmap -vv --reason -Pn -T4 -sV -p 49669 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49669/tcp_49669_rpc_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49669/xml/tcp_49669_rpc_nmap.xml" 10.10.10.134

nmap -vv --reason -Pn -T4 -sV -p 49670 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49670/tcp_49670_rpc_nmap.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp49670/xml/tcp_49670_rpc_nmap.xml" 10.10.10.134


```