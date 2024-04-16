nome = str(input('Digite o nome de uma pessoa: ')).strip()
nome = nome.split()
print('O primeiro nome é {}'.format(nome[0]))
print('O último nome é {}'.format(nome[len(nome)-1]))
