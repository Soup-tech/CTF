# Intro to Windows

## File Systems
There are some notable Folders in Windows:
<ul>
	<li>PerfLogs: Stores system issues and other reports on performance</li>
	<li>Program Files and Program Files (x86): Where programs are installed</li>
	<li>Users: Stored where users are created</li>
	<li>Windows: Folder which contains the code that runs the operating system</li>
</ul>

## File Permissions
File peermissions can be set by an administrator or a privileged account. These permissions are applied to:
<ul>
	<li>Users</li>
	<li>Groups</li>
</ul>

Permissions that can be set:
<ul>
	<li>Full Control: allows the users/groups to set the ownership of the folder, set permissions, modify, read, write, and execute files</li>
	<li>Modify: allows users/groups to modify, read, write and execute files</li>
	<li>Read and Execute: allows users/groups to execute files</li>
	<li>List folders contents: allows users/groups to list the contents (files, folders, subfolders) of a folder</li>
	<li>Read: only allow for reading files</li>
	<li>Write: write data to the specific folder</li>
</ul>

In Powershell and cmd, you can use <b>icacls</b> to check file and folder permissions.
```
icacls C:\Important
C:\Important BUILTIN\Users: (OI)(CI)(M)
	NT AUTHORITY\SYSTEM: (I)(OI)(CI)(F)
	BUILTIN\Administrator: (I)(OI)(CI)(F)
	BUILTIN\Users: (I)(OI)(CI)(RX)
	BUILTIN\Users: (I)(CI)(AD)
	BUILTIN\Users: (I)(CI)(WD)
	CREATOR OWNER: (I)(OI)(CI)(IO)(F)
```
The permissions are as follows:
<ul>
	<li>I - permission inherited from the parent container</li>
	<li>F - full access (full control)</li>
	<li>M - Modify right/access</li>
	<li>OI - object inherit</li>
	<li>IO - inherit only</li>
	<li>CI - container inherit</li>
	<li>RX - read and execute</li>
	<li>AD - append data (add subdirectories)</li>
	<li>WD - write data and add files</li>
</ul>