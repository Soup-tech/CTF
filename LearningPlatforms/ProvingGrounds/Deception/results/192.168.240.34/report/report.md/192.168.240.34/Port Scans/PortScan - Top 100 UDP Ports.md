```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/_top_100_udp_nmap.txt" -oX "/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/xml/_top_100_udp_nmap.xml" 192.168.240.34
```

[/home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/_top_100_udp_nmap.txt](file:///home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.92 scan initiated Sun Apr 10 00:03:03 2022 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/_top_100_udp_nmap.txt -oX /home/kali/Documents/CTF/LearningPlatforms/ProvingGrounds/Deception/results/192.168.240.34/scans/xml/_top_100_udp_nmap.xml 192.168.240.34
Increasing send delay for 192.168.240.34 from 50 to 100 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 192.168.240.34 from 100 to 200 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 192.168.240.34 from 200 to 400 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 192.168.240.34 from 400 to 800 due to 11 out of 11 dropped probes since last increase.
adjust_timeouts2: packet supposedly had rtt of -88932 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -88932 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -81767 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -81767 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -185623 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -185623 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -252705 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -252705 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -242773 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -242773 microseconds.  Ignoring time.
Nmap scan report for 192.168.240.34
Host is up, received user-set (0.049s latency).
Scanned at 2022-04-10 00:03:03 EDT for 326s

PORT      STATE         SERVICE         REASON              VERSION
7/udp     open|filtered echo            no-response
9/udp     closed        discard         port-unreach ttl 63
17/udp    closed        qotd            port-unreach ttl 63
19/udp    closed        chargen         port-unreach ttl 63
49/udp    closed        tacacs          port-unreach ttl 63
53/udp    open|filtered domain          no-response
67/udp    open|filtered dhcps           no-response
68/udp    closed        dhcpc           port-unreach ttl 63
69/udp    open|filtered tftp            no-response
80/udp    closed        http            port-unreach ttl 63
88/udp    open|filtered kerberos-sec    no-response
111/udp   closed        rpcbind         port-unreach ttl 63
120/udp   closed        cfdptkt         port-unreach ttl 63
123/udp   open|filtered ntp             no-response
135/udp   open|filtered msrpc           no-response
136/udp   open|filtered profile         no-response
137/udp   closed        netbios-ns      port-unreach ttl 63
138/udp   closed        netbios-dgm     port-unreach ttl 63
139/udp   closed        netbios-ssn     port-unreach ttl 63
158/udp   open|filtered pcmail-srv      no-response
161/udp   closed        snmp            port-unreach ttl 63
162/udp   closed        snmptrap        port-unreach ttl 63
177/udp   closed        xdmcp           port-unreach ttl 63
427/udp   closed        svrloc          port-unreach ttl 63
443/udp   closed        https           port-unreach ttl 63
445/udp   closed        microsoft-ds    port-unreach ttl 63
497/udp   closed        retrospect      port-unreach ttl 63
500/udp   closed        isakmp          port-unreach ttl 63
514/udp   open|filtered syslog          no-response
515/udp   closed        printer         port-unreach ttl 63
518/udp   closed        ntalk           port-unreach ttl 63
520/udp   open|filtered route           no-response
593/udp   closed        http-rpc-epmap  port-unreach ttl 63
623/udp   open|filtered asf-rmcp        no-response
626/udp   closed        serialnumberd   port-unreach ttl 63
631/udp   open|filtered ipp             no-response
996/udp   open|filtered vsinet          no-response
997/udp   open|filtered maitrd          no-response
998/udp   open|filtered puparp          no-response
999/udp   open|filtered applix          no-response
1022/udp  open|filtered exp2            no-response
1023/udp  open|filtered unknown         no-response
1025/udp  closed        blackjack       port-unreach ttl 63
1026/udp  closed        win-rpc         port-unreach ttl 63
1027/udp  open|filtered unknown         no-response
1028/udp  closed        ms-lsa          port-unreach ttl 63
1029/udp  closed        solid-mux       port-unreach ttl 63
1030/udp  open|filtered iad1            no-response
1433/udp  closed        ms-sql-s        port-unreach ttl 63
1434/udp  open|filtered ms-sql-m        no-response
1645/udp  closed        radius          port-unreach ttl 63
1646/udp  open|filtered radacct         no-response
1701/udp  closed        L2TP            port-unreach ttl 63
1718/udp  closed        h225gatedisc    port-unreach ttl 63
1719/udp  closed        h323gatestat    port-unreach ttl 63
1812/udp  closed        radius          port-unreach ttl 63
1813/udp  closed        radacct         port-unreach ttl 63
1900/udp  closed        upnp            port-unreach ttl 63
2000/udp  open|filtered cisco-sccp      no-response
2048/udp  closed        dls-monitor     port-unreach ttl 63
2049/udp  open|filtered nfs             no-response
2222/udp  closed        msantipiracy    port-unreach ttl 63
2223/udp  closed        rockwell-csp2   port-unreach ttl 63
3283/udp  open|filtered netassistant    no-response
3456/udp  open|filtered IISrpc-or-vat   no-response
3703/udp  closed        adobeserver-3   port-unreach ttl 63
4444/udp  closed        krb524          port-unreach ttl 63
4500/udp  closed        nat-t-ike       port-unreach ttl 63
5000/udp  open|filtered upnp            no-response
5060/udp  open|filtered sip             no-response
5353/udp  open|filtered zeroconf        no-response
5632/udp  closed        pcanywherestat  port-unreach ttl 63
9200/udp  closed        wap-wsp         port-unreach ttl 63
10000/udp closed        ndmp            port-unreach ttl 63
17185/udp closed        wdbrpc          port-unreach ttl 63
20031/udp closed        bakbonenetvault port-unreach ttl 63
30718/udp closed        unknown         port-unreach ttl 63
31337/udp closed        BackOrifice     port-unreach ttl 63
32768/udp closed        omad            port-unreach ttl 63
32769/udp closed        filenet-rpc     port-unreach ttl 63
32771/udp open|filtered sometimes-rpc6  no-response
32815/udp closed        unknown         port-unreach ttl 63
33281/udp closed        unknown         port-unreach ttl 63
49152/udp closed        unknown         port-unreach ttl 63
49153/udp open|filtered unknown         no-response
49154/udp open|filtered unknown         no-response
49156/udp open|filtered unknown         no-response
49181/udp open|filtered unknown         no-response
49182/udp open|filtered unknown         no-response
49185/udp closed        unknown         port-unreach ttl 63
49186/udp closed        unknown         port-unreach ttl 63
49188/udp closed        unknown         port-unreach ttl 63
49190/udp closed        unknown         port-unreach ttl 63
49191/udp closed        unknown         port-unreach ttl 63
49192/udp open|filtered unknown         no-response
49193/udp open|filtered unknown         no-response
49194/udp closed        unknown         port-unreach ttl 63
49200/udp open|filtered unknown         no-response
49201/udp closed        unknown         port-unreach ttl 63
65024/udp closed        unknown         port-unreach ttl 63
Too many fingerprints match this host to give specific OS details
TCP/IP fingerprint:
SCAN(V=7.92%E=4%D=4/10%OT=%CT=%CU=9%PV=Y%DS=2%DC=T%G=N%TM=6252583D%P=x86_64-pc-linux-gnu)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 2 hops

TRACEROUTE (using port 4444/udp)
HOP RTT      ADDRESS
1   49.46 ms 192.168.49.1
2   49.49 ms 192.168.240.34

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Apr 10 00:08:29 2022 -- 1 IP address (1 host up) scanned in 325.95 seconds

```
