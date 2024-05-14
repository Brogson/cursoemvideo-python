n = 0
soma = 0
c = 0
while n != 999:
    n = int(input('Digite um número menor que 999: '))
    if n != 999:
        soma += n
        c += 1
print('A soma de todos os {} números foi: {}'.format(c, soma))
