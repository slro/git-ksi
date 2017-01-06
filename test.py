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

def assign_uid_to_generated_signature(signature):
    id_assignin_json = {"metadata":{},"signature": signature}
    r = requests.put(url, headers=headers, json=id_assignin_json)
    return json.loads(r.text)

def get_signature(id):
    url_id= url+"/"+id
    r = requests.get(url_id, headers=headers)
    return json.loads(r.text)


response = create_new_signature("1pUmHbQszLgVWYKsoRxx2QdzYa49TKAbO8y/QlbpDn4=",0)

print(assign_uid_to_generated_signature(response['signature']))
print(get_signature(response['id']))