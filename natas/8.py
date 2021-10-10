#!/usr/bin/python3

import requests
import re
import base64

def hex_to_char(ct):
    pt = ""
    for i in range(0,len(ct),2):
        pt+=chr(int(ct[i:i+2],16))
    return pt


username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = 'http://%s.natas.labs.overthewire.org' % username

response = requests.get(url+'/index-source.html', auth = (username, password))
content = response.text
# print(content)

ct = re.findall('encodedSecret&nbsp;=&nbsp;"(.*)\";<br /><br />',content)[0]
# print(ct)

pt = hex_to_char(ct)
# print(pt)

pt = pt[::-1]
# print(pt)

pt = base64.b64decode(pt)
# print(pt)

data = {'secret':pt,'submit':'submit'}
response = requests.post(url, auth = (username, password),data=data)
content = response.text
# print(content)

pwd = re.findall('natas9 is (.*)', content)[0]
print(pwd)
