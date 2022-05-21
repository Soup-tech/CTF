# Reconnaissance
This phase helps us understand the attack surface, technologies used, and, in some cases, discover development environments or forgotten and unmaintained infrastructure. 

As we discover new assets, we will need to fingerprint the technologies in use, look for hidden pages/directories, etc., which may lead us to discover another  subdomain and start the process over again.

## Useful tools
Subfinder
amass
dig
assetfinder
sublist3r <- Primary subdomain enumeration tool to use
chaos
TheHarvester

## Whois
Considered as the "white pages" for domain names. It is a transaction-oriented query/response protocol listening on TCP port 43 by default. 

```bash
$ whois facebook.com
```

There is a lot of good information output from a whois query but some there are some items of interest:
- Organization
- Locations
- Domain Email Address
- Registrar Email Address
- Phone Number
- Language
- Registrar
- Name Domain
- DNSSEC
- Name Servers

## Nslookup and Dig
Nslookup is a command line tool that allows us to query various DNS requests. Dig is another command line tool that shows more information by querying a specific nameserver. 

### A Record
An A record points a domain or subdomain at an IP address.
```bash
$ nslookup -query=A company.com
```

```bash
$ dig A company.com @8.8.8.8
```

### PTR Record
DNS A records are stored under the given domain name, DNS PTR records are stored under the IP address - reversed.

```bash
$ nslookup -query=PTR 31.13.66.35
```

```bash
$ dig -x 31.13.66.35 @8.8.8.8
```

### Any Record
You can use the Any record to query all records.

```bash
$ dig any company.com @8.8.8.8
```

### TXT Record
The DNS TXT record lets the domain administrator enter text into the Domain Name System. Primarily used for human-readable notes

```bash
$ nslookup -query=txt google.com
```

```bash
$ dig txt google.com @8.8.8.8
```

### MX Records
Mail Exchange (MX) records directs email to a mail server. This indicates how emails should be routed in accordance with the Simple Mail Transfer Protocol (SMTP).

```bash
$ nslookup -query=mx company.com
```

```bash
$ dig mx facebook.com @8.8.8.8
```

## Passive Subdomain Enumeration
Mapping subdomains increase attack surface and may uncover hidden management backend panels or intranet web applications that network administrators expected to keep hidden using the "security by obscurity" strategy.

### VirusTotal
[VirusTotal](https://www.virustotal.com/gui/home/search) maintains its DNS replication service, which is developed by preserving DNS resolutions made when users visit URLs given by them.

Putting the domain name into the search bar and clicking "Relations" tab shows information about a domain.

### Project Sonar
Rapid7's Project Sonar is a security research project that conducts internet-wide surveys across various services and protocols to gather insight into worldwide vulnerability exposures.

This is all processed through Rapid7's API endpoints:
```
https://sonar.omnisint.io/subdomains/{domain} - All subdomains for a given domain
https://sonar.omnisint.io/tlds/{domain}       - All tlds found for a given domain
https://sonar.omnisint.io/all/{domain}        - All results across all tlds for a given domain
https://sonar.omnisint.io/reverse/{ip}        - Reverse DNS lookup on IP address
https://sonar.omnisint.io/reverse/{ip}/{mask} - Reverse DNS lookup of a CIDR range
```

Find subdomains
```bash
$ curl -s https://sonar.omnisint.io/subdomains/target.com | jq -r '.[]' | sort -u
```

Find TLDs
```bash
$ curl -s https://sonar.omnisint.io/tlds/target.com | jq -r '.[]' | sort -u
```

### TheHarvester
There really is no better tool for recon than TheHarvester. The tool collects, emails, names, subdomains, IP addresses, and URLs from various public data sources for passive info gathering.

TheHarvester uses the following modules:
- Baidu
- Bufferoverun
- Crtsh
- Hackertarget
- 0tx
- Rapiddns
- Sublist3r
- Threatcrowd
- Threatminer
- Trello
- Urlscan
- Vhost
- Virustotoal
- Zoomeye

You can then automate this process by inserting all of these module names into a file called 'sources.txt'

```bash
$ cat sources.txt | while read source; do theHarvester -d "company.com" -b $source -f "${source}_company.com"; done
```


## Active Infrastructure Identification
Netcraft can offer us information about servers without even interacting with them. We can use the service by visiting https://sitereport.netcraft.com

Interesting information includes:
- Background
- Network
- Hosting History

Pay special attention to the latest IP used. Sometimes we can spot the actual IP address from the webserver before it is placed behind a load balancer, web applicaiton firewall, or IDS, allowing us to connect directly to it if the configuration allows it.


### Web Servers 
Discovering as much information as possible from the web server is crucial. URL rewriting, load balancing, script engines used on the server, or an Intrusion Detection System (IDS). Most of this information can come from looking at the headers when cURL'ing the index of the web server. Some headers to keep in mind:
- X-powered-By: This header can what the web application is using. Such as PHP, ASP.NET, JSP, etc.
- Cookies: Attractive values to look at as each technology by default has its cookies. Some are ASPSESSIONID, PHPSESSID, JSESSION

[WhatWeb](https://morningstarsecurity.com/research/whatweb) is a great tool for recognizing web technologies.

```bash
$ whatweb -a 4 https://facebook.com -v
```

Other good tools include 
- [WebApplyzer](https://www.wappalyzer.com) - Very handy browser extension 
- [WafW00f](https://github.com/EnableSecurity/wafw00f) - A web application firewall fingerprinting tool 


## Active Subdomain Enumeration
We can probe the infrastructure managed by the target organization or the 3rd party DNS servers we have previously identified. 

### Zone Transfer
Zone transfer is how a secondary DNS server receives information from the primary DNS server and updates it. It is a master-slave approach and is used to organize DNS servers within a domain, with slaves receiving updated DNS information from the master DNS. The master DNS server should be configured to enable zone transfers from secondary (slave) DNS servers. 

The AV for performing a zone transfer looks like:
1. Identify nameserver
```bash
$ nslookup -type=ns zonetransfer.me

Non-authoritative answer:
zonetransfer.me nameserver = nsztm2.digi.ninja.
zonetransfer.me nameserver = nsztm1.digi.ninja.
```

2. Testing for ANY and AXFR Zone Transfer
```bash
$ nslookup -type=any -query=axfr zonetransfer.me nsztm1.digi.ninja
```


## Virtual Hosts
Virtual host is a feature to host several websites on a single webserver. Two ways to configure virtual host:

### IP Based
A host can have multiple network interfaces. The servers or virtual servers running on the host can bind to one or more IP addresses. From the client POV, servers are independent of one another

### Name-Based
The distinction for which domain the service was requested is made at the application layer. There can be multiple domain names, such as admin.inlanefreight.htb and backup.inlanefrieght.htb, can refer to the same IP. 
On the server the vHost are seperated into different folders. 

### vHost Discovery
You can discover both types of vHosts using fuff
```bash
$ fuff -w /opt/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://inlanefreight.htb -H "Host: FUZZ.inlanefreight.htb" 
```
