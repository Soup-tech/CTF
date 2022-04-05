#!/usr/bin/env python3
import string

def modInverse(a,m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1): return x
    return -1


mapping = string.ascii_uppercase + string.digits + "_"

numbers = open('message.txt','r').readlines()
numbers = "".join(numbers)
numbers = numbers.split(' ')
del numbers[-1]
numbers = list(map(int,numbers))

flag = ""
for n in numbers:
    n = n % 41
    m = modInverse(n,41)
    flag += mapping[m - 1]

print(flag)
