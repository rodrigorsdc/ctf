import base64

key = 'eDWo'
inp = '{"showpassword":"yes","bgcolor":"#ffffff"}'
out = ''
for i in range(len(inp)):
    out = out + chr(ord(inp[i]) ^ ord(key[i % len(key)]))

print(base64.b64encode(bytes(out, 'ascii')))
