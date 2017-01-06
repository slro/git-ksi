#!/usr/bin/env python3

import requests
import json

credentials = '"ot.S1xpgT":"xRKHrjcSFTw6"'

url = "https://tryout-catena-db.guardtime.net/api/v1/signatures"
headers = {"Content-Type": "application/json",
           "Accept": "application/json",
           "Authorization":'Basic '+credentials}


def create_new_signature(hash, level):
    json_for_signature_creation = {'dataHash': {'algorithm':'SHA-256', 'value': hash}, 'metadata': {}, 'level': 0}
    r = requests.post(url, headers=headers, json=json_for_signature_creation)
    return json.loads(r.text)

#print(create_new_signature("1pUmHbQszLgVWYKsoRxx2QdzYa49TKAbO8y/QlbpDn4=",0))