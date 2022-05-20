#!/usr/bin/env python3

user_input = "AMFh1m(jc_1gFg4ns}kqgt0{,[5n1}du"
encrypted_bytes = [0x29,0x38,0x2b,0x1e,0x06,0x42,0x05,0x5d,0x07,0x02,0x31,0x42,0x0f,0x33,0x0a,0x55,0x00,0x00,0x15,0x1e,0x1c,0x06,0x1a,0x43,0x13,0x59,0x36,0x54,0x00,0x42,0x15,0x11,0x00]
key = "humans"
fin = 0

key_bytes = []
for s in key:
    key_bytes.append(ord(s))

user_input_bytes = []
for s in user_input:
    user_input_bytes.append(ord(s))

print(user_input_bytes)
print(key_bytes)
print(encrypted_bytes)

password = ""
for i in range(0,32):
    password += chr(encrypted_bytes[i] ^ key_bytes[i%6])
    print(chr(encrypted_bytes[i] ^ key_bytes[i % 6]))
    #fin += int(chr(encrypted_bytes[i] ^ key_bytes[i % 6]))

print(password)
#print(fin)
