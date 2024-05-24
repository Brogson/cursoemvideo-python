l0 = list()
l1 = list()
l2 = list()
pares = 0
maiorv2 = 0

for c in range(0, 3):
    n = int(input(f'Digite o valor para a coluna {c} da linha 0: '))
    l0.append(n)
    if n % 2 == 0:
        pares += n
for d in range(0, 3):
    n = int(input(f'Digite um valor para a coluna {d} da linha 1: '))
    if d == 0:
        maiorv2 = n
    else:
        if n > maiorv2:
            maiorv2 = n
    l1.append(n)
    if n % 2 == 0:
        pares += n
for e in range(0, 3):
    n = int(input(f'Digite um valor para a coluna {e} da linha 2: '))
    l2.append(n)
    if n % 2 == 0:
        pares += n

print(l0)
print(l1)
print(l2)

valores3 = l0[2] + l1[2] + l2[2]
print(f'A soma dos valores pares é  {pares}.')
print(f'A terceira coluna soma: {valores3}')
print(f'O maior valor da segunda linha é {maiorv2}')