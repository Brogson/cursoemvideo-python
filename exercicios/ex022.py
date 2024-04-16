nome = str(input('Digite o seu none completo: '))
print('Em letras maiúsculas: {}'.format(nome.upper()))
print('Em letras minúsculas: {}'.format(nome.lower()))
print('O nome possui {} letras'.format(len(nome.replace(' ', ''))))
dividido = nome.split()
pnome = dividido[0]
print('O primeiro nome é {} e tem {} letras'.format(pnome, len(pnome)))
