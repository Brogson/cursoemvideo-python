n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print('O primeiro valor ({}) é maior.'.format(n1))
elif n2 > n1:
    print('O segundo valor ({}) é maior.'.format(n2))
else:
    print('Os dois valores ({} e {}) são iguais.'.format(n1, n2))
