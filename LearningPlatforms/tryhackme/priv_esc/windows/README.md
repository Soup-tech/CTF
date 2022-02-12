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
DLL hijacking is an effective technique that can allow you to inject code into an applicaitno. Some Window executables will use Dynamic Link Libraries (DLL) when running. DLLs are files that store additional functions that suppor tht emain funciton of the .exe file. DLL's however cannot be ran directly and require a .exe to run it. If we switch the legitmate DLL file with a specially crafted DLL file, our code will be run by the applicaiton. DLL hijacking requires an application (typically an exe file) that either has a missing DLL file, or where the search order can be used to insert the malicious DLL file. 

### Introduction to DLL Files
Something to keep in mind is that missing a DLL will not always result in an error. When launched, the application will look for DLL files it needs and, while a missing critical DLL file can stop the application from running, lesser important ones may not result in visible errors.<br>
A DLL hijacking scenario consists of replacing a legitimate DLL file with a malicious DLL file that will be called by the executable and run. A successful DLL hijacking attack can be summarized as:
1. An applicaiton that uses one or more DLL files
2. A way to manipulate these DLL files
Manipulation may include replaces an existing file or creating a file in the location where the applicaiton is looking for it.
In summary , for standard desktop applications, Windows will follow one of the orders listed below depending on if the SafeDllSearchMode is enabled or not.<br>
If SafeDllSearchMode is enabled, the search order is follow:
1. The directory from which the application loaded
2. The system directory. Use the GetSystemDirectory function to get the path of this directory
3. The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched. 
4. The Windows directory. Use the GetWindowsDirectory function to get the path of this directory
5. The current directory
6. The directories that are listed in the PATH environment variable. Note that this does not include the per-applciation path specified by the App Paths registry key. The App Paths key is not sued when computing the DLL search path. 

If SafeDllSearchMode is disabled, the search order is as follows:
1. The directory from which the application loaded.
2. The current directory.
3. The system directory. Use the GetSystemDirectory function to get the path of this directory.
4. The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.
5. The Windows directory. Use the GetWindowsDirectory function to get the path of this directory.
6. The directories that are listed in the PATH environment variable. Note that this does not include the per-application path specified by the App Paths registry key. The App Paths key is not used when computing the DLL search path.
For example, if our application.exe requires the app.dll file to run, it will look for the app.dll file first in the directory from which it is launched. If this does not return any match for app.dll, the search will continue in the above-specified order. If the user privileges we have on the system allow us to write to any folder in the search order, we can have a possible DLL hijacking vulnerability. An important note is that the application should not be able to find the legitimate DLL before our modified DLL.<br>

### Finding DLL Hijacking Vulnerabilities
The first step is to use a tool you can use to find potential DLL hijacking vulnerabilities is Process Monitor (ProcMon). This software requires Admin rights, so this is something you will have to load on your test machine and conduct research. Look for .exe trying to launch certain .dll but cannot find said .dll. The second step is to create this missing .dll file. It is important that we have write permissions for any folder we wish to use for DLL hijacking.

### Creating the Malicious DLL file
An example of a potential DLL file is below:
```C
#include <windows.h>

BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved) {
    if (dwReason == DLL_PROCESS_ATTACH) {
        system("cmd.exe /k whoami > C:\\Temp\\dll.txt");
        ExitProcess(0);
    }
    return TRUE;
}
```