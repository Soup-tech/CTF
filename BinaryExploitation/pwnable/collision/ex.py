#!/usr/bin/env python3

from pwn import *

# Payload
payload = p32(0x6c5cec8)*4 + p32(0x6c5cecc)

### Connection
# username: col
# Hostname: pwnable.kr (You can also use the IP: 128.61.240.205; I got this with dig)
# Password: guest
# Port: 2222
conn = ssh('col','pwnable.kr',password='guest',port=2222)

### Run the remote program
# Executable to run: col
# Argument list: col (name of the executable), payload
program = conn.process(executable='./col', argv=['col',payload])

# Grab the returned output
flag = program.recv()
print(flag.decode())

program.close()
conn.close()