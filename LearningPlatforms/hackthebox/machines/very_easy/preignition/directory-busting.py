#!/usr/bin/env python3

import sys
import requests

extension_switch = False

def help():
	print("./scan.py [HOST] [WORDLIST]")
	sys.exit(-1)

def error(msg):
	print(f"Error: {msg}")
	sys.exit(-1)

def arguments():

	if ('-x' in argv):
		extension_switch = True

	return

def hit(r,ext):

	if (r.status_code == 200):
		print(f"{ext}\t200")

	return

argv = sys.argv

# Correct paremters
if (len(argv) < 3):
	help()

# Which switches are active
arguments()

url = argv[1]
if ("http://" not in url):
	error("Unrecognized host")

wordlist = argv[2]

for line in open(wordlist):
	line = line.strip()

	if ('#' in line):
		continue

	r = requests.get(f"{url}/{line}/")
	hit(r, line)

	if (extension_switch):
		extensions = argv.index('-x') + 1

		if (',' in extensions):

			extensions_lst = extensions.split(',')
			for ext in extensions_lst:
				url = f"{url}/{line}.{ext}"
				r = requests.get(url)
				hit(r, f"{line}.{ext}")

		else:
			url = f"{url}/{line}.{extensions}"
			r = requests.get(url)
			hit(r,f"{line}.{extensions}")
