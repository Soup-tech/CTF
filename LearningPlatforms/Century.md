# Century
Learning PowerShell. I learned bash using [OverTheWire](https://overthewire.org/wargames/) and I am really glad there is a similar platform for PowerShell. 
[UnderTheWire](https://underthewire.tech/) is OverTheWire counterpart. I'll be loggin what I do to solve these problems. 

## Century1
```
The password for Century2 is the build version of the instance of PowerShell installed on this system.
```
Researching...
```ps1
$PSVersionTable

Name                           Value                                                                                        
----                           -----                                                                                        
PSVersion                      5.1.14393.4583                                                                               
PSEdition                      Desktop                                                                                      
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}                                                                      
BuildVersion                   10.0.14393.4583                                                                              
CLRVersion                     4.0.30319.42000                                                                              
WSManStackVersion              3.0                                                                                          
PSRemotingProtocolVersion      2.3                                                                                          
SerializationVersion           1.1.0.1
```
BuildVersion is 10.0.14393.4583

## Century2
```
The password for Century3 is the name of the built-in cmdlet that performs the wget like function within PowerShell PLUS the name of the file on the desktop.
```
Looking at cmdlets, the **Invoke-WebRequest** seems like the command to use. The file is 443 thus: **invoke-webrequest443** gives me the credentials to Century3.

## Century3
```
The password for Century4 is the number of files on the desktop.
```
Quick Googling shows two cmdlets. The first is **Get-ChildItem** which is similar to the ls command on Linux. We can pipe this cmdlet into the **Measure-Object** cmdlet.
```ps1
(Get-ChildItem | Measure-Object)

Count    : 123                                                                                                              
Average  :                                                                                                                  
Sum      :                                                                                                                  
Maximum  :                                                                                                                  
Minimum  :                                                                                                                  
Property :
```

## Century4
```
The password for Century5 is the name of the file within a directory on the desktop that has spaces in its name.
```
This was a pretty simple one as it is very similar to Linux.
```ps1
cd ".\Can You Open Me"
```
The file is **5548**.
