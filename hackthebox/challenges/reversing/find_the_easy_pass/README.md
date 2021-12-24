# Find The Easy Pass

## Hint
```
Find the password (say PASS) and enter the flag in the form HTB{PASS}
```

## Procedure
Checking what type of file I am working with:
```bash
file EasyPass.exe
EasyPass.exe: PE32 executable (GUI) Intel 80386, for MS Windows
```
Verifying that this is a PE32:
```bash
xxd EasyPass.exe | head

00000000: 4d5a 5000 0200 0000 0400 0f00 ffff 0000  MZP.............
00000010: b800 0000 0000 0000 4000 1a00 0000 0000  ........@.......
00000020: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000030: 0000 0000 0000 0000 0000 0000 0001 0000  ................
00000040: ba10 000e 1fb4 09cd 21b8 014c cd21 9090  ........!..L.!..
00000050: 5468 6973 2070 726f 6772 616d 206d 7573  This program mus
00000060: 7420 6265 2072 756e 2075 6e64 6572 2057  t be run under W
00000070: 696e 3332 0d0a 2437 0000 0000 0000 0000  in32..$7........
00000080: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000090: 0000 0000 0000 0000 0000 0000 0000 0000  ................
```
Which is a DOS MZ executable and its descendants are NE and PE.
The application <a href="https://wiki.winehq.org/Ubuntu">Wine</a> allows us to run Windows applications on Linux.
```bash
wine EasyPass.exe
```
Presents us with a password window. It's possible that the password is in cleartext. Running the strings Unix command gives a lot. So I threw the application into Ghidra.