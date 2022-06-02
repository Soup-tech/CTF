```bash
[*] ssh on tcp/22

	[-] Bruteforce logins:

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 22 -o "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp22/tcp_22_ssh_hydra.txt" ssh://10.10.10.134

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 22 -O "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp22/tcp_22_ssh_medusa.txt" -M ssh -h 10.10.10.134

[*] msrpc on tcp/135

	[-] RPC Client:

		rpcclient -p 135 -U "" 10.10.10.134

[*] netbios-ssn on tcp/139

	[-] Nmap scans for SMB vulnerabilities that could potentially cause a DoS if scanned (according to Nmap). Be careful:

		nmap -vv --reason -Pn -T4 -sV -p 139 --script="smb-vuln-ms06-025" --script-args="unsafe=1" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp139/tcp_139_smb_ms06-025.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp139/xml/tcp_139_smb_ms06-025.xml" 10.10.10.134

		nmap -vv --reason -Pn -T4 -sV -p 139 --script="smb-vuln-ms07-029" --script-args="unsafe=1" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp139/tcp_139_smb_ms07-029.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp139/xml/tcp_139_smb_ms07-029.xml" 10.10.10.134

		nmap -vv --reason -Pn -T4 -sV -p 139 --script="smb-vuln-ms08-067" --script-args="unsafe=1" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp139/tcp_139_smb_ms08-067.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp139/xml/tcp_139_smb_ms08-067.xml" 10.10.10.134

[*] microsoft-ds on tcp/445

	[-] Lookup SIDs

		lookupsid.py [username]:[password]@10.10.10.134

	[-] Nmap scans for SMB vulnerabilities that could potentially cause a DoS if scanned (according to Nmap). Be careful:

		nmap -vv --reason -Pn -T4 -sV -p 445 --script="smb-vuln-ms06-025" --script-args="unsafe=1" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp445/tcp_445_smb_ms06-025.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp445/xml/tcp_445_smb_ms06-025.xml" 10.10.10.134

		nmap -vv --reason -Pn -T4 -sV -p 445 --script="smb-vuln-ms07-029" --script-args="unsafe=1" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp445/tcp_445_smb_ms07-029.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp445/xml/tcp_445_smb_ms07-029.xml" 10.10.10.134

		nmap -vv --reason -Pn -T4 -sV -p 445 --script="smb-vuln-ms08-067" --script-args="unsafe=1" -oN "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp445/tcp_445_smb_ms08-067.txt" -oX "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp445/xml/tcp_445_smb_ms08-067.xml" 10.10.10.134

[*] http on tcp/5985

	[-] (feroxbuster) Multi-threaded recursive directory/file enumeration for web servers using various wordlists:

		feroxbuster -u http://10.10.10.134:5985 -t 10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -o /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_feroxbuster_dirbuster.txt

	[-] Credential bruteforcing commands (don't run these without modifying them):

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 5985 -o "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_auth_hydra.txt" http-get://10.10.10.134/path/to/auth/area

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 5985 -O "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_auth_medusa.txt" -M http -h 10.10.10.134 -m DIR:/path/to/auth/area

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 5985 -o "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_form_hydra.txt" http-post-form://10.10.10.134/path/to/login.php:"username=^USER^&password=^PASS^":"invalid-login-message"

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 5985 -O "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_form_medusa.txt" -M web-form -h 10.10.10.134 -m FORM:/path/to/login.php -m FORM-DATA:"post?username=&password=" -m DENY-SIGNAL:"invalid login message"

	[-] (nikto) old but generally reliable web server enumeration tool:

		nikto -ask=no -h http://10.10.10.134:5985 2>&1 | tee "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_nikto.txt"

	[-] (wpscan) WordPress Security Scanner (useful if WordPress is found):

		wpscan --url http://10.10.10.134:5985/ --no-update -e vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive --plugins-version-detection aggressive -f cli-no-color 2>&1 | tee "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp5985/tcp_5985_http_wpscan.txt"

	[-] Bruteforce logins:

		crackmapexec winrm 10.10.10.134 -d <domain> -u /usr/share/seclists/Usernames/top-usernames-shortlist.txt -p /usr/share/seclists/Passwords/darkweb2017-top100.txt

	[-] Check login (requires credentials):

		crackmapexec winrm 10.10.10.134 -d <domain> -u <username> -p <password> -x "whoami"

	[-] Evil WinRM (gem install evil-winrm):

		evil-winrm -u <user> -p <password> -i 10.10.10.134

		evil-winrm -u <user> -H <hash> -i 10.10.10.134

[*] http on tcp/47001

	[-] (feroxbuster) Multi-threaded recursive directory/file enumeration for web servers using various wordlists:

		feroxbuster -u http://10.10.10.134:47001 -t 10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -o /home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp47001/tcp_47001_http_feroxbuster_dirbuster.txt

	[-] Credential bruteforcing commands (don't run these without modifying them):

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 47001 -o "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp47001/tcp_47001_http_auth_hydra.txt" http-get://10.10.10.134/path/to/auth/area

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 47001 -O "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp47001/tcp_47001_http_auth_medusa.txt" -M http -h 10.10.10.134 -m DIR:/path/to/auth/area

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 47001 -o "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp47001/tcp_47001_http_form_hydra.txt" http-post-form://10.10.10.134/path/to/login.php:"username=^USER^&password=^PASS^":"invalid-login-message"

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 47001 -O "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp47001/tcp_47001_http_form_medusa.txt" -M web-form -h 10.10.10.134 -m FORM:/path/to/login.php -m FORM-DATA:"post?username=&password=" -m DENY-SIGNAL:"invalid login message"

	[-] (nikto) old but generally reliable web server enumeration tool:

		nikto -ask=no -h http://10.10.10.134:47001 2>&1 | tee "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp47001/tcp_47001_http_nikto.txt"

	[-] (wpscan) WordPress Security Scanner (useful if WordPress is found):

		wpscan --url http://10.10.10.134:47001/ --no-update -e vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive --plugins-version-detection aggressive -f cli-no-color 2>&1 | tee "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bastion/results/10.10.10.134/scans/tcp47001/tcp_47001_http_wpscan.txt"

	[-] Bruteforce logins:

		crackmapexec winrm 10.10.10.134 -d <domain> -u /usr/share/seclists/Usernames/top-usernames-shortlist.txt -p /usr/share/seclists/Passwords/darkweb2017-top100.txt

	[-] Check login (requires credentials):

		crackmapexec winrm 10.10.10.134 -d <domain> -u <username> -p <password> -x "whoami"

	[-] Evil WinRM (gem install evil-winrm):

		evil-winrm -u <user> -p <password> -i 10.10.10.134

		evil-winrm -u <user> -H <hash> -i 10.10.10.134

[*] msrpc on tcp/49664

	[-] RPC Client:

		rpcclient -p 49664 -U "" 10.10.10.134

[*] msrpc on tcp/49665

	[-] RPC Client:

		rpcclient -p 49665 -U "" 10.10.10.134

[*] msrpc on tcp/49666

	[-] RPC Client:

		rpcclient -p 49666 -U "" 10.10.10.134

[*] msrpc on tcp/49667

	[-] RPC Client:

		rpcclient -p 49667 -U "" 10.10.10.134

[*] msrpc on tcp/49668

	[-] RPC Client:

		rpcclient -p 49668 -U "" 10.10.10.134

[*] msrpc on tcp/49669

	[-] RPC Client:

		rpcclient -p 49669 -U "" 10.10.10.134

[*] msrpc on tcp/49670

	[-] RPC Client:

		rpcclient -p 49670 -U "" 10.10.10.134


```