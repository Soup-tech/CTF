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
Servers are simply programs that run in the backgroun, accepting input or performing regular tasks. If vulnerable services are running as root, exploiting them can lead to command execution as root.
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
 ssh -R <local-port>:127.0.0.1:<service-port> <username>@<local-machine>
 ```
 First, determine what applications are running on what port:
 ```bash
 netstat -nl
 
 tcp        0      0 127.0.0.1:3306           0.0.0.0:*   
 ```
 Which means MySQL is only listening on localhost. You can port-forward all information from your host.
 
 ## Weak File Permission
 System files can be taken advantage of to perform privilege escalation if the permissions on them are too weak. If a system file has confidential information we can read, it may be used to gain access to the root account. If a system file can be written to, we may be able to modify the way the OS works and gain root access that way.<br><br>
 For example, the <b>/etc/shadow</b> file contains user password hashes, and by default is not readable by any user except for root. If we are able to read the contents of the /etc/shadow file, we might be able to crack the root user's password hash. If we are able to modify the /etc/shadow file, we can replace the root user's password hash with one we know.<br>
 If we can write the contents of /etc/shadow for instance, we can replace the root user hash with our own.
 ```bash
 mkpasswd -m sha-512 newpassword
 ```
