import requests
import json
import time

f = open('token.txt', 'r')
token = f.read()
f.close()

# получить список своих друзей
params = {
    'v': '5.52', 
    'access_token': token, 
    'count': 10, 
    'order': 'hints'
}
r = requests.get('https://api.vk.com/method/friends.get', params=params)
friends = json.loads(r.content)

max_count = 0
max_user_id = 0
for friend in friends['response']['items']:
    params = {'user_id': friend, 'v': '5.52', 'access_token': token}
    r = requests.get('https://api.vk.com/method/friends.get', params=params)
    f = json.loads(r.content)
    count = f['response']['count']  # получить число друзей у друга
    if count > max_count:
        max_count = count
        max_user_id = friend
    print('.', end='')
    time.sleep(1)

print()
print(max_user_id, max_count)