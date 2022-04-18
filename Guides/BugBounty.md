# Bug Bounty
This will be a collection of tips, tricks and methodology for bug bounties. All the information here comes from [HTB Academy - Bug Bounty Program](https://academy.hackthebox.com/).
Only new stuff that I learned will exist here as well as a general procedure that I'll try to follow. This will also contain links to other repo's which contain cheat sheets. 

## Procedure
https://github.com/harshinsecurity/web-pentesting-checklist

https://alike-lantern-72d.notion.site/Web-Application-Penetration-Testing-Checklist-4792d95add7d4ffd85dd50a5f50659c6

## Using Web Proxies
- **Intercepting Responses**: You can intercept web server responses before it reaches the client. This is useful when we want to change the apperance, enable/disable certain fields, and change the overall behavior of the web app.
- **Automatic Modification**: You can apply certain modifications for all requests/responses based on a ruleset. This can be useful when a web application blocks a certain header or feature (such as a User-Agent). Change this (Proxy>Options>Match and Replace)
- **ProxyChain**: proxychains is probably the simplest way to route all traffic from the command line to a proxy. Edit /etc/proxychain.conf, comment out *socks4 127.0.0.1 9050* and add *http 127.0.0.1 8080*. It is also a good idea to enable quite mode. To route traffic
```bash
proxychains curl http://SERVER_IP:PORT/
```
