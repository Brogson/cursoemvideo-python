n = int(input('Digite um número para calcular seu fatorial: '))
c = n-1
while c > 0:
    print('{} x {} = {}'.format(n, c, n*c))
    n = n * c
    c -= 1
print('Fim do programa')
