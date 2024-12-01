import requests

url = 'http://natas17.natas.labs.overthewire.org'
user = 'natas17'
password = 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC'

data = {'username' : '" <sdcript> </script>', 'debug' : '1'}
response = requests.get(url, auth=(user, password), params=data)

print(response.text)
data = {'username' : 'natas17'} 
response2 = requests.get(url, auth=(user, password), params=data)

print(response2.text)
print(response.content == response2.content)
