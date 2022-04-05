picobrowser

> connection
```
	https://jupiter.challenges.picoctf.org/problem/26704/
```
> hint
```
	You don't need to download a new web browser
```

> We click on 'flag' and get an error message: "You're not picobrowser! Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
> I'm guessing the User-Agent in the HTTP header needs to be modified to "picobrowser". Burpsuite is probably the best way to go about this
> Capture the GET request and modify the User-Agent to "picobrowser"
```HTTP
	GET /flag HTTP/1.1
	Host: jupiter.challenges.picoctf.org
	User-Agent: picobrowser
	Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
	Accept-Language: en-US,en;q=0.5
	Accept-Encoding: gzip, deflate
	Referer: https://jupiter.challenges.picoctf.org/problem/26704/flag
	Connection: close
	Cookie: _ga=GA1.2.1242253668.1636508294; _gid=GA1.2.2129270114.1637119771
	Upgrade-Insecure-Requests: 1
	Cache-Control: max-age=0
```

> We get the flag from the response
> flag
```
	picoCTF{p1c0_s3cr3t_ag3nt_e9b160d0}
```