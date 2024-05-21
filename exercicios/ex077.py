vogais = ''
tupla = ('aprender',
         'programar',
         'linguagem',
         'curso',
         'gratis',
         'praticar',
         'estudar',
         'trabalhar')
for c in tupla:
    for cont in range(0, len(c)):
        if c[cont] in 'aeiou':
            vogais += c[cont] + ' '
    print(f'A palavra {c} tem como vogais: {vogais.upper()}')
    vogais = ''
print('Fim do programa')
