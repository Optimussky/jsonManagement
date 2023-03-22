# readJsonFile.py

import json

with open('users.json') as f:
    payload = json.load(f)

    for user in payload['users']:
        print(user)


