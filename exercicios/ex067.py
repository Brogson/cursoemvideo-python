n = 0
c = 1
while True:
    n = int(input('Digite um número para consultar sua tabuada: '))
    if n <= 0:
        break
    print(f'A tabuada de {n} é:')
    while c <= 10:
        res = n * c
        print(f'{n} x {c} = {res}')
        c += 1
    c = 1
    print('Para finalizar digite um valor negativo abaixo')
print('Fim do programa!')
