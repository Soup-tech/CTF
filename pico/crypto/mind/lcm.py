#!/usr/bin/env python3

def leastOfTwo(p, q):
	if (p > q):
		return p
	else:
		return q



p = 61 - 1
q = 53 - 1


guess = leastOfTwo(p, q)
while True:
	print(f"Guessing: {guess}")
	if ((guess % p == 0) and (guess % q == 0)):
		print(f"Least Common Multiple: {guess}")
		break
	else:
		guess += 1