# log4j

## Reconnaissance
First thing is to scan and enumerate the target using nmap. CVE-2021-44228, dubbed "Log4Shell", impacts the Java logging package log4j versions 2.0-beta9 through 2.12.1 and 2.13.0 through 2.15.0<br>
```bash
nmap -p- -sV 10.10.98.169
```
nmap results are found in <a href="log4j.nmap">log4j.nmap</a><br>

## Discovery
