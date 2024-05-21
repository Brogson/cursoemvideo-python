pares = 0
tupla = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')), int(input('Digite um último valor: ')))
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 apareceu pela primeira ves na {tupla.index(3) + 1}ª posição')
else:
    print(f'O número 3 não foi adicionado à tupla')
for c in tupla:
    if c % 2 == 0:
        pares += 1
print(f'A quantidade de números pares foi: {pares}')
