sexo = str(input('Digite o seu sexo: [M/F] ')).upper()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Ocorreu algum erro na sua digitação! Por favor repita: [M/F]')).upper()
print('Muito obrigado pela resposta')
