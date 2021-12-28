#!/usr/bin/env python3

import requests

url = 'http://10.129.218.159/'
for line in open('/opt/wordlist/directory-list-2.3-medium.txt'):
	line = line.strip()
	
	if ('#' in line):
		continue

	r = requests.get(f"{url}{line}")
	if (r.status_code == 200 or r.status_code == 302):
		print(f"{line}\t{r.status_code}")