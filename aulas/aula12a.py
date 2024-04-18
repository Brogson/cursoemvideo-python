nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem comum')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}!'.format(nome))
