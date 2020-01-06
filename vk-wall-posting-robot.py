import requests
import json
import time
import random

f = open('token.txt', 'r')
token = f.read()
f.close()

params = {
    'v': '5.52',
    'access_token': token,
    'owner_id': 382533516,
    'message': random.randint(1, 10000000),
    'attachments': 'photo382533516_457240293',
    'lat': 55.753663,
    'long': 37.619854,
}

r = requests.get('https://api.vk.com/method/wall.post', params=params)
j = json.loads(r.content)
print('post_id:', j['response']['post_id'])