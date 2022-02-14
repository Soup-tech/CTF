# Linux Privilege Escalation
This is a guide a made while studying for my OSCP. The lectures that I took notes from are <a href="https://www.udemy.com/course/linux-privilege-escalation/">here</a>. The setup and workshop environment are <a href="https://github.com/sagishahar/lpeworkshop">here</a>.

## Kernel Exploits
Kernels are the core of any OS. Exploiting a kernel vulnerability can result in execution as the root user. Finding and using kernel exploits is a simple process:
1. Enumerate kernel version (uname -a)
2. Find matching exploits (Google, ExploitDB, GitHub)
3. Compile and run
Beware: Kernel exploits can often be unstable and may be one-shot or cause a system crash. Should be a last resort. <br>
A good way to find kernel exploits is by using linux-exploit-suggester
```bash
./linux-exploit-suggester -k <kernel-version>
```
