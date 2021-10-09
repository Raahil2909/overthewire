#!/usr/bin/python3

import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = 'http://%s.natas.labs.overthewire.org' % username

# coming from natas7
# hdr = {'Referer':'http://natas7.natas.labs.overthewire.org/'}
# cookie = {'loggedin':'1'}
response = requests.get(url, auth = (username, password))
content = response.text
print(content)

"""

pwd = re.findall('natas7 is (.*)<', content)[0]
print(pwd)
"""

