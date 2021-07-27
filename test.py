
import json

f = open('Database.json')
userdatas = json.load(f)

find = [user for user in userdatas if user['name'] == 'user1']

print(find)