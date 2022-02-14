# Leviathan
Connect using ssh -p 2223 leviathan#@leviathan.labs.overthewire.org<br>
## leviathan0
```
leviathan0:leviathan0
```
Upon logging in, there is a hidden directory <b>.backup</b> which contains a bunch of bookmarks. I used the following command and got lucky:
```bash
cat bookmarks.html | grep password
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is rioGegei8m" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

## leviathan1
```
leviathan1:rioGegei8m
```
There is an application <b>check</b>. Check has it's suid bit set for leviathan2 meaning a privilege escalation will take place. Running the program gives us a prompt for a password. I open up this applicaiton in GDB a bit of reading (no pun intended), I find a strcmp take place.
```bash
   0x0804857f <+68>:    call   0x80483c0 <printf@plt>
   0x08048584 <+73>:    add    esp,0x10
   0x08048587 <+76>:    call   0x80483d0 <getchar@plt>
   0x0804858c <+81>:    mov    BYTE PTR [ebp-0xc],al
   0x0804858f <+84>:    call   0x80483d0 <getchar@plt>
   0x08048594 <+89>:    mov    BYTE PTR [ebp-0xb],al
   0x08048597 <+92>:    call   0x80483d0 <getchar@plt>
   0x0804859c <+97>:    mov    BYTE PTR [ebp-0xa],al
   0x0804859f <+100>:   mov    BYTE PTR [ebp-0x9],0x0
   0x080485a3 <+104>:   sub    esp,0x8
   0x080485a6 <+107>:   lea    eax,[ebp-0x10]
   0x080485a9 <+110>:   push   eax
   0x080485aa <+111>:   lea    eax,[ebp-0xc]
   0x080485ad <+114>:   push   eax
   0x080485ae <+115>:   call   0x80483b0 <strcmp@plt>
   0x080485b3 <+120>:   add    esp,0x10
   0x080485b6 <+123>:   test   eax,eax
   0x080485b8 <+125>:   jne    0x80485e5 <main+170>
   0x080485ba <+127>:   call   0x80483e0 <geteuid@plt>
   0x080485bf <+132>:   mov    ebx,eax
   0x080485c1 <+134>:   call   0x80483e0 <geteuid@plt>
   0x080485c6 <+139>:   sub    esp,0x8
   0x080485c9 <+142>:   push   ebx
   0x080485ca <+143>:   push   eax
   0x080485cb <+144>:   call   0x8048410 <setreuid@plt>
```
Checking the two values that get pushed on the stack yields the password I inputted and the supposed correct passowrd
```bash
(gdb) x/s $ebp-0x10
0xffffd6a8:     "sex"
```
Inputting this password yields an upgraded shell.

## leviathan2
```
leviathan2:ougahZi8Ta
```