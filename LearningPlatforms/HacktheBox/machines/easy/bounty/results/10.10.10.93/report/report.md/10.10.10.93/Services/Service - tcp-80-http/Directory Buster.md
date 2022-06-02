```bash
feroxbuster -u http://10.10.10.93:80/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"
```

[/home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt](file:///home/kali/Documents/Repositories/CTF/LearningPlatforms/hackthebox/machines/easy/bounty/results/10.10.10.93/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt):

```
200      GET     1624l    16517w   780732c http://10.10.10.93/merlin.jpg
200      GET       32l       53w      630c http://10.10.10.93/
301      GET        2l       10w      156c http://10.10.10.93/aspnet_client => http://10.10.10.93/aspnet_client/
200      GET       22l       58w      941c http://10.10.10.93/transfer.aspx
301      GET        2l       10w      156c http://10.10.10.93/uploadedfiles => http://10.10.10.93/uploadedfiles/
301      GET        2l       10w      156c http://10.10.10.93/uploadedFiles => http://10.10.10.93/uploadedFiles/
301      GET        2l       10w      156c http://10.10.10.93/UploadedFiles => http://10.10.10.93/UploadedFiles/
200      GET       22l       58w      941c http://10.10.10.93/Transfer.aspx
301      GET        2l       10w      156c http://10.10.10.93/Aspnet_client => http://10.10.10.93/Aspnet_client/
301      GET        2l       10w      156c http://10.10.10.93/aspnet_Client => http://10.10.10.93/aspnet_Client/
200      GET       22l       58w      941c http://10.10.10.93/TRANSFER.aspx
301      GET        2l       10w      156c http://10.10.10.93/ASPNET_CLIENT => http://10.10.10.93/ASPNET_CLIENT/
301      GET        2l       10w      156c http://10.10.10.93/Aspnet_Client => http://10.10.10.93/Aspnet_Client/
301      GET        2l       10w      156c http://10.10.10.93/Uploadedfiles => http://10.10.10.93/Uploadedfiles/

```
