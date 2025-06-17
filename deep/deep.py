resp = input('Qual é a Grande Pergunta da Vida, do Universo e Tudo Mais? ')
resp = resp.strip().lower().replace('-', ' ')

respostas = ('42', 'forty two', 'fortytwo')

if resp in respostas:
    print('Yes')
else:
    print('No')
