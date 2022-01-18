# Windows Privilege Escalation Guide

Typical privilege escalation methodology:
1. Enumerate the current user's privileges and resources it can access
2. If the antivirus software allows it, run an automated enumeration script such as winPEAS or PowerUp.ps1
3. If the initial enumeration and scripts do not uncover an obvious strategy, try a different approach (such as a <a href="https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md">manual check list</a>)

## Information Gathering
### User Enumeration
> whoami /priv
Current user privileges
> net users
List users
> net user username (e.g. net user Administrator)
List details of a user
> qwinsta (the query session command can be used the same way)
Other users logged in simultaneously
> net localgroup
User groups defined on the system
> net localgroup groupname (e.g. net localgroup Administrators)
List members of a specific group

### Collecting System Information
The <b>systeminfo</b> command will return an overview of the target system. On some targets, teh amount of data returned by this command can be overwhelming, so you can always grep the output as seen below:
```bash
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
```

### Searching for Files
Some low hanging fruit may be:
```bash
findstr /si password *.txt
```
Changing the extension to .txt, .xml, .ini, .config, .xls are all good places to start

### Patch Level
Microsoft releases patches all the time. A missing critical patch on the target can be an easily exploitable ticket to privilege escalation. You can list updates installed on the target system.
```bash
wmic qfe get Caption,Description,HotFixID,InstalledOn
```
WMIC is a command-line tool on Windes that provides an interace for Windows Management Instrumentation (WMI). WMI is used for management operations on Windows and is a powerful tool worth knowing. 

### Network Connections
To list all listening ports on the target system. 
```bash
netstat -ano
```
-a: Display all active connections
-n: Prevent name resolution
-o: Displays the process ID using each listed connection
Any port listed as "LISTENING" that was not discoved with the external port scan can present a potential local service. If you uncover such a service, you can try port forwarding to connect and potentially expliot it. 

### Scheduled Tasks
Some tasks are scheduled to run at predefined times. If they run with privileged account (e.g. the System Administrator account) and the executable they run can be modified by the current user you have, an easy path for privilege escalation can be available.
The <b>schtasks</b> command can be used to query scheduled tasks.
```bash
schtasks /query /fo LIST /v
```

### Drivers
Drivers are additional software installed to allow the OS to interact with an external device. While the OS may be updated regularly, drivers may not be. Listing available drivers on the target system can also preset a privilege escalation vector. 
```bash
driverquery
```

### Antivirus
Antivirus will typically not detect you if you accessed the machine in some formal way (Like RDP or SSH) but will detect you if you use some form of trojan. However, to reach higher privilege level, you may need to run scripts or other tools on the target system. Therefore, it is good to check if any antivirus is present. 
This is done with two approaches: Looking for the antivirus specifically or listing all running services and checking which ones may belong to antivirus software. This may require some research on services running. Windows Defender is a famous AV. You can search for a service named "windefend" and return its current state.
```bash
sc query windefend
```
Another way will allow you to detect antivirus software without prior knowledge aobut its service name.
```bash
sc queryex type=service
```

## Tools of the Trade
There are some pretty cool scripts to automate enumeration.

### WinPEAS
Used to enumerate the target system to uncover privilege escalation paths. Note that Windows Defender detects and disables winPEAS.

### PowerUp
Run with the <b>Invoke-AllChecks</b> option that will perform all possible checks on the target sytem or use it to conduct specific checks (e.g. the <b>Get-UnquotedService</b> option is to only look for potential unquoted service path vulnerabilities). To run PowerUp on the target, you may need to bypass the execution policy restrictions. To achieve this, you can launch PowerShell using commands below
```ps1
powershell.exe -nop -exec bypass
```

### Windows Exploit Suggester
Most scripts that require an upload may be deleted by the AV. Using Windows Exploit Suggester (WES) runs on your local attack machine and will not be detected.  To use:
```bash
windows-exploit-suggester.py -update
windows-exploit-suggester.py --database 2021-09-21-mssb.xls --systeminfo sysinfo_output.txt
```

### Metasploit
If you have a Meterpreter shell on the target system, you can use the <b>multi/recon/local_exploit_suggester</b> module to list vulnerabilities that may affect the target system and allow you to elvate your privileges on the target system.

## Vulnerable Software
Users and organizations are unlikely to update software and drivers as often as their OS. You can use te <b>wmic</b> tool seen previously to list software installed on the target system and its versions. Use <b>wmic product</b> to dump information about all installed software. 
```bash
wmic product
```
Filter info using <b>wmic product get name,version,number</b>.<br>
```bash
wmic product get name,version,vendor
```
Because of backwards compatibility issues, the <b>wmic product</b> command may not return all installed programs. To have a better understanding of the target system <b>wmic service list brief</b>.<br>
```bash
wmic service list brief 
```
You can of course grep the output for running services by adding a <b>findstr</b>
```bash
wmic service list brief | findstr "Running"
```
More information on any service, you can simply use the <b>sc qc</b> command.
```bash
sc qc RemoteMouseService
```
Otheways in PowerShell
```bash
Get-Service | ? {$_.status -eq "Running"} | select -First 2 | fl
```
Get version information with PowerShell
```bash
(Get-Item -Path "C:\Path\To\Program.exe").VersionInfo
```
After that, you have a few resources to find vulnerabilities and exploits agains software installed on the system.
1. Searchsploit
2. Metasploit
3. Exploit-DB
4. Github
5. Google

## DLL Hijacking
