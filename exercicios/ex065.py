soma = 0
n = 0
c = 0
maior = 0
menor = 0
q = 'S'
while q == 'S':
    n = int(input('Digite um número: '))
    soma += n
    c += 1
    if c == 1:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    q = str(input('Quer digitar mais valores? [S/N]')).upper()
print('A média dos {} números digitados é: {}'.format(c, soma/c))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
