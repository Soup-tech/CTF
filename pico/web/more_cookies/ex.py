#!/usr/bin/env python3

import requests
from base64 import b64decode
from base64 import b64encode
from tqdm import tqdm

def bitFlip(pos, bit, data):
	raw = b64decode(b64decode(data).decode())
	list1 = bytearray(raw)

	list1[pos] = list1[pos] ^ bit
	raw = bytes(list1)

	return b64encode(b64encode(raw)).decode()

url = 'http://mercury.picoctf.net:43275/'
auth_name = 'TlV1WXQvSFB1cSswNW9CNDlPWW1oTndvbEZmMTBFMVBGSXF6ejdQMnljUUVjcElDeVlmQ1lPMTE0RXl4SzgycFM3YjJDR2RYSkpnNTU3eG9ZNXg3SjVkS3hBWFB1MkpkZStlVVl6a3JPT1hJVE1TZnZ4WE40VGVxVExoK0dMQzU='


for i in tqdm(range(10)):
	for j in tqdm(range(128)):
		auth_name_cookie = bitFlip(i, j, auth_name)
		# print(f"Trying: {auth_name_cookie} Number {j} Position {i}")

		cookies = {'auth_name':str(auth_name_cookie)}
		r = requests.get(url,cookies=cookies)
		if ('picoCTF{' in r.text):
			break

	
print(r.text)