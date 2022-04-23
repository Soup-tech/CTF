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

## Century5
```
The password for Century6 is the short name of the domain in which this system resides in PLUS the name of the file on the desktop.
```
First, the file on the Desktop is **3347**.
Using the **Get-WmiObject** cmdlet with the Class Win32_NTDomain gives the domain name.
```ps1
Get-WmiObject -Class Win32_NTDomain

ClientSiteName          : Default-First-Site-Name                                                                           
DcSiteName              : Default-First-Site-Name                                                                           
Description             : underthewire                                                                                      
DnsForestName           : underthewire.tech                                                                                 
DomainControllerAddress : \\192.99.167.156                                                                                  
DomainControllerName    : \\UTW                                                                                             
DomainName              : underthewire                                                                                      
Roles                   :                                                                                                   
Status                  : OK
```
The Get-WmiObject (Windows Management Instrumentation) gets instances of WMI classes or information about the available classes. The Win32_NTDomain class represents the a Windows domain.

## Century6
```
The password for Century7 is the number of folders on the desktop.
```
This was similar to Century3
```ps1
Get-ChildItem | Measure-Object

Count    : 197                                                                                                              
Average  :                                                                                                                  
Sum      :                                                                                                                  
Maximum  :                                                                                                                  
Minimum  :                                                                                                                  
Property :
```

## Century7
```
The password for Century8 is in a readme file somewhere within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.
```
**Get-ChildItem** cmdlet seems to be a 'roided version of ls.
```ps1
Get-ChildItem readme*

    Directory: C:\users\century7\Downloads                                                                                  
                                                                                                                            
                                                                                                                            
Mode                LastWriteTime         Length Name                                                                       
----                -------------         ------ ----                                                                       
-a----        8/30/2018   3:29 AM              7 Readme.txt                                                                 
-a----        2/12/2022   8:59 PM              2 Readme2.txt
```
The contents of Readme.txt was **7points**

## Century8
```
The password for Century9 is the number of unique entries within the file on the desktop.
```
