#!/usr/bin/python3
import string
mapping = string.ascii_uppercase + string.digits + "_"

modded_nums = []
flag = ""
for n in open('message.txt','r'):
    n = n.strip()
    n = int(n) % 37
    flag += mapping[n]

print(flag)
