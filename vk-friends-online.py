import requests
import json

f = open('token.txt', 'r')
token = f.read()
f.close()

r = requests.get('https://api.vk.com/method/friends.getOnline?v=5.52&access_token=' + token)
friends = json.loads(r.content)

online = len(friends['response'])
print('Всего друзей онлайн:', online)