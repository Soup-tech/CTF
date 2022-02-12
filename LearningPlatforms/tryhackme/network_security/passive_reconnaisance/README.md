# Passive Reconnaissance

## Passive vs Active
Preliminary survey to gather information about a target. Two types of reconnaissance:<br>
1. Passive reconnaissance
2. Active reconnaissance
In passive, you rely on publicly available knowledge. Information you can gather without direcly engaging the target. This inlcudes:
<ul>
	<li>Looking up DNS records of a domain from a public DNS server</li>
	<li>Checking job ads related to the target website</li>
	<li>Reading news articles about the target company</li>
</ul>
Active recon, on the other hand, cannot be achieved so discreetly. It requires direct engagement. Examples of active recon:
<ul>
	<li>Connecting to one of the company servers such as HTTP, FTP, and SMTP</li>
	<li>Calling the company to gain information (Social Engineering)</li>
	<li>Entering company premises</li>
</ul>

## Whois
WHOIS is a request and response protocol that follows <a href="https://datatracker.ietf.org/doc/html/rfc3912">RFC 3912</a>. WHOIS listens on port 43. The domain registrar is responsible for maintaining the WHOIS records for the domain names it is leasing. Replies with various information such as:
<ul>
	<li>Registrar: Via which registrar was the domain name registered?</li>
	<li>Contact info of registrant: Name, organization, address, phone, among other things</li>
	<li>Creation, update, and expiration dates: When was the domain name first registered? When was it last updated? When does it need to be renewed</li>
	<li>Name server: which server to ask to resolve the domain name?</li>
</ul>

```bash
whois tryhackme.com

Domain Name: TRYHACKME.COM              
Registry Domain ID: 2282723194_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.namecheap.com
Registrar URL: http://www.namecheap.com
Updated Date: 2021-05-01T19:43:23Z                                                                                
Creation Date: 2018-07-05T19:46:15Z
Registry Expiry Date: 2027-07-05T19:46:15Z
Registrar: NameCheap, Inc.                     
Registrar IANA ID: 1068                  
Registrar Abuse Contact Email: abuse@namecheap.com
Registrar Abuse Contact Phone: +1.6613102107                                                                      
Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
Name Server: KIP.NS.CLOUDFLARE.COM
Name Server: UMA.NS.CLOUDFLARE.COM                                                                                
DNSSEC: unsigned                
URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/
>>> Last update of whois database: 2022-01-21T07:48:52Z <<<
[...]
Domain name: tryhackme.com                                                                                           
Registry Domain ID: 2282723194_DOMAIN_COM-VRSN                                                                       
Registrar WHOIS Server: whois.namecheap.com                                                                          
Registrar URL: http://www.namecheap.com                                                                              
Updated Date: 2021-05-01T19:43:23.31Z
Creation Date: 2018-07-05T19:46:15.00Z
Registrar Registration Expiration Date: 2027-07-05T19:46:15.00Z
Registrar: NAMECHEAP INC
Registrar IANA ID: 1068
Registrar Abuse Contact Email: abuse@namecheap.com
Registrar Abuse Contact Phone: +1.9854014545
Reseller: NAMECHEAP INC
Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
Registry Registrant ID: 
Registrant Name: Redacted for Privacy
Registrant Organization: Privacy service provided by Withheld for Privacy ehf
Registrant Street: Kalkofnsvegur 2 
Registrant City: Reykjavik
Registrant State/Province: Capital Region
Registrant Postal Code: 101
Registrant Country: IS
Registrant Phone: +354.4212434
Registrant Phone Ext: 
Registrant Fax: 
Registrant Fax Ext: 
Registrant Email: a70a4ff6d25041a48378997194f9e834.protect@withheldforprivacy.com
Registry Admin ID: 
Admin Name: Redacted for Privacy
Admin Organization: Privacy service provided by Withheld for Privacy ehf
Admin Street: Kalkofnsvegur 2 
Admin City: Reykjavik
Admin State/Province: Capital Region
Admin Postal Code: 101
Admin Country: IS
Admin Phone: +354.4212434
Admin Phone Ext: 
Admin Fax: 
Admin Fax Ext: 
Admin Email: a70a4ff6d25041a48378997194f9e834.protect@withheldforprivacy.com
Registry Tech ID: 
Tech Name: Redacted for Privacy
Tech Organization: Privacy service provided by Withheld for Privacy ehf
Tech Street: Kalkofnsvegur 2 
Tech City: Reykjavik
Tech State/Province: Capital Region
Tech Postal Code: 101
Tech Country: IS
Tech Phone: +354.4212434
Tech Phone Ext: 
Tech Fax: 
Tech Fax Ext: 
Tech Email: a70a4ff6d25041a48378997194f9e834.protect@withheldforprivacy.com
Name Server: kip.ns.cloudflare.com
Name Server: uma.ns.cloudflare.com
```
Some things of note:
<ul>
	<li><b>Registrar WHOIS Server: whois.namecheap.com</b>: This is who is maintaining the WHOIS record for this domain name.</li>
	<li>The registrant name and email is redacted for privacy reasons</li>
	<li><b>Domain Name</b>: Name which should be query'd for DNS record look-ups</li>
</ul>
This gives a few attack surfaces, such as social engineering or technical attacks. For example, you may consider an attack against the email server of the admin user or the DNS servers. 

## nslookup and dig
Find the IP address of a domain using <b>nslookup</b>, which stands for <b>Name Server Look Up</b>.
```bash
nslookup tryhackme.com 

Server:         192.168.1.254
Address:        192.168.1.254#53

Non-authoritative answer:
Name:   tryhackme.com
Address: 172.67.27.10
Name:   tryhackme.com
Address: 104.22.54.228
Name:   tryhackme.com
Address: 104.22.55.228
Name:   tryhackme.com
Address: 2606:4700:10::6816:37e4
Name:   tryhackme.com
Address: 2606:4700:10::6816:36e4
Name:   tryhackme.com
Address: 2606:4700:10::ac43:1b0a
```

The general syntax is: <b>nslookup OPTIONS DOMAIN_NAME 	SERVER</b>
The three main parameters:
<ul>
	<li>OPTIONS: Contain the query type as shown in the table below. For instance, you can use <b>A</b> for IPv4 and <b>AAAA</b> for IPv6.</li>
	<li>DOMAIN_NAME: is the domain name you are looking up</li>
	<li>SERVER: DNS server you want to query. There are public DNS servers such as Cloudflare's <b>1.1.1.1</b> and <b>1.0.0.1</b>. Google's <b>8.8.8.8</b> and <b>8.8.4.4</b> and many others</li>
</ul>
<ul>Query Type
	<li>A: IPv4 Address</li>
	<li>AAAA: IPv6 Address</li>
	<li>CNAME: Canonical Name</li>
	<li>MX: Mail Server</li>
	<li>SOA: Start of Authority</li>
	<li>TXT: TXT Records</li>
</ul>

```bash
nslookup -type=MX tryhackme.com

Non-authoritative answer:
tryhackme.com   mail exchanger = 10 alt4.aspmx.l.google.com.
tryhackme.com   mail exchanger = 10 alt3.aspmx.l.google.com.
tryhackme.com   mail exchanger = 5 alt2.aspmx.l.google.com.
tryhackme.com   mail exchanger = 1 aspmx.l.google.com.
tryhackme.com   mail exchanger = 5 alt1.aspmx.l.google.com.
```
Which shows that TryHackMe current email configuration uses Google.<br>

For more DNS queries and additional functionality, you can use <b>dig</b>, the acronm for "Domain Information Groper". The syntax is <b>dig @SERVER DOMAIN_NAME TYPE</b>

```bash
dig tryhackme.com MX

; <<>> DiG 9.17.21-1-Debian <<>> tryhackme.com MX
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 34908
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;tryhackme.com.                 IN      MX

;; ANSWER SECTION:
tryhackme.com.          300     IN      MX      10 alt3.aspmx.l.google.com.
tryhackme.com.          300     IN      MX      5 alt2.aspmx.l.google.com.
tryhackme.com.          300     IN      MX      10 alt4.aspmx.l.google.com.
tryhackme.com.          300     IN      MX      1 aspmx.l.google.com.
tryhackme.com.          300     IN      MX      5 alt1.aspmx.l.google.com.
```

## DNSDumpster
Domains may contain subdomains that can reveal more about a target. Subdomains are typically not maintained or updated regularly, making them for vulnerable. You can try bruteforcing subdomains but this may take some time. You can use <a href="https://dnsdumpster.com/">DNSDumpster</a>. Using the graph shows a better representation of the data DNSDumpster can provide.

## Shodan.io
<a href="https://www.shodan.io">Shodan.io</a> is one of the best tools for passive recon. Shodan tries to connect to every device reachable online to build a search engine of connected "things" in contrast with a search engine for web pages. From Shodan we can learn a few things:
<ul>
	<li>IP Address</li>
	<li>Hosting comapany</li>
	<li>Geographical Location</li>
	<li>Server type and version</li>
</ul>