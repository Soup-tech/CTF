# Bug Bounty
This will be a collection of tips, tricks and methodology for bug bounties. All the information here comes from [HTB Academy - Bug Bounty Program](https://academy.hackthebox.com/).
Only new stuff that I learned will exist here as well as a general procedure that I'll try to follow. This will also contain links to other repo's which contain cheat sheets. 

## Procedure
https://github.com/harshinsecurity/web-pentesting-checklist

https://alike-lantern-72d.notion.site/Web-Application-Penetration-Testing-Checklist-4792d95add7d4ffd85dd50a5f50659c6

## Using Web Proxies
- **Intercepting Responses**: You can intercept web server responses before it reaches the client. This is useful when we want to change the apperance, enable/disable certain fields, and change the overall behavior of the web app.
- **Automatic Modification**: You can apply certain modifications for all requests/responses based on a ruleset. This can be useful when a web application blocks a certain header or feature (such as a User-Agent). Change this (Proxy>Options>Match and Replace)
- **OWASP - Zap**: I would really only recommend using Zap for it's Spidering and Active Scanning features. It is overall a good application (nice GUI, open source, free) but I am already too dedicated to Burp. Perhaps in another life...


## Information Gathering

### Whois
We can consider WHOIS as the "white pages" for domain names. It is a TCP-based transaction-oriented query/response protocol listening on TCP port 43 by default. We can use it for querying databases containing domain names, IP addresses, or autonomous systems and provide information services to Internet users. The protocol is defined in RFC 3912. 
```bash
$ whois <target>
```

Information to pay attention to in the results of a whois query:
- Organization
- Locations
- Domain Email Address
- Registrar Email Address
- Phone Number
- Language
- Registrar
- New Domain
- DNSSEC
- Name Servers

### Domain Name System (DNS)
Considered the internet phonebook.

There is a heirarchy of names in DNS structure. The system's root, the highest level, is unnamed.

Top-Level Domains nameservers, might be compared to a single shelf of books in a library.
