import os

resposta = input('File name: ').strip().lower()

tipos = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

#Não preciso armazenar esta variavel
_, ext = os.path.splitext(resposta)

if ext in tipos:
    print(tipos[ext])
else:
    print('application/octet-stream')
