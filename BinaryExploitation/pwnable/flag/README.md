# flag

## Hint
```
	Papa brought me a packed present! let's open it.
	This is reversing task. all you need is binary
```

## Procedure
Identify the type of file I'm reversing.<br>

```bash
file flag
flag: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
```
This is executable and linking file (ELF) and is 64-bit<br>
This file being statically linked means all library modules used in the program are copied into the final executable. Whereas dynamically linked means the libraries are linked during runtime.<br>

Check binary security
```bash
checksec --file=flag
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable  FILE
No RELRO        No canary found   NX disabled   No PIE          No RPATH   No RUNPATH   No Symbols      No      0               0       flag
```
Breaking down this output:<br>
<b>No RELRO</b>: Relocation Read-Only (RELRO) makes the Global Offset Table (GOT) partially readable or fully readable. This security measure prevents the GOT from being overwritten.<br>
<b>STACK CANARY</b>: A stack canary is a secret value placed on the stack which changes every runtime. Prior to a function return, the stack canary is checked and if modified the program ends.<br>
<b>NX disabled</b>: The NX bit marks certain areas in memory as not executable. This is important because it prevents attackers from injecting and executing shellcode into an executable.<br>
<b>PIE</b>: Position-Independent Executable (PIE) where if set, loads the file into a different location in memory. If this is not set, the file is loaded into the same memory area.<br><br>

This file has no security measures.<br>

Running the file:
```bash
I will malloc() and strcpy the flag there. take it.
```
Maybe the flag is stored in the heap?<br>
Running strings on this file and seeing if the file is stored in cleartext I found:
```bash
UPX 3.08 Copyright (C) 1996-2011 the UPX Team. All Rights Reserved.
````
From https://upx.github.io/<br>
"UPX is a free, portable, extendable, high-performance executable packer for several executable formats."<br>
I first need to decompress this executable using UPX.<br>
After doing so my file command yields:
```bash
file decompressed_file
decompressed_file: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, for GNU/Linux 2.6.24, BuildID[sha1]=96ec4cc272aeb383bd9ed26c0d4ac0eb5db41b16, not stripped
```

I crack open GDB<br>
```bash
maximillian@Bear:~/Documents/repos/CTF/pwnable/flag$ gdb -q ./decompressed_file
Reading symbols from ./decompressed_file...
(No debugging symbols found in ./decompressed_file)
(gdb) disass main
Dump of assembler code for function main:
   0x0000000000401164 <+0>:     push   rbp
   0x0000000000401165 <+1>:     mov    rbp,rsp
   0x0000000000401168 <+4>:     sub    rsp,0x10
   0x000000000040116c <+8>:     mov    edi,0x496658
   0x0000000000401171 <+13>:    call   0x402080 <puts>
   0x0000000000401176 <+18>:    mov    edi,0x64
   0x000000000040117b <+23>:    call   0x4099d0 <malloc>
   0x0000000000401180 <+28>:    mov    QWORD PTR [rbp-0x8],rax
   0x0000000000401184 <+32>:    mov    rdx,QWORD PTR [rip+0x2c0ee5]        # 0x6c2070 <flag>
   0x000000000040118b <+39>:    mov    rax,QWORD PTR [rbp-0x8]
   0x000000000040118f <+43>:    mov    rsi,rdx
   0x0000000000401192 <+46>:    mov    rdi,rax
   0x0000000000401195 <+49>:    call   0x400320
   0x000000000040119a <+54>:    mov    eax,0x0
   0x000000000040119f <+59>:    leave  
   0x00000000004011a0 <+60>:    ret    
End of assembler dump.
```
I see a comment labeled flag. Breakpoint at 0x0000000000401184 and then examining what is at 0x6c2070. After messing around with the different output formats (hex,decimal,etc) I get the flag
```bash
(gdb) x/s *0x6c2070
0x496628:       "UPX...? sounds like a delivery service :)"
```
## Flag
UPX...? sounds like a delivery service :)<br>

## Things I learned
This is a great resource for learning CTF related info: https://ctf101.org/<br>

