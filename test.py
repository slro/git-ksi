#!/usr/bin/env python3

import requests
import json

url = "https://tryout-catena-ksi.guardtime.net/api/v1/signature"
headers = {"Content-Type": "application/json",
           "Accept": "application/json",
           "Authorization":'Basic "ot.S1xpgT:xRKHrjcSFTw6"'}

with open("dataHash.json") as json_file:
    data = json.load(json_file)

r = requests.post(url,headers=headers,json=data)
print(r.text)