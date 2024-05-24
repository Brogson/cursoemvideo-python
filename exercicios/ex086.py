l0 = list()
l1 = list()
l2 = list()


for c in range(0, 3):
    l0.append(int(input(f'Digite o valor para a coluna {c} da linha 0: ')))

for d in range(0, 3):
    l1.append(int(input(f'Digite um valor para a coluna {d} da linha 1: ')))

for e in range(0, 3):
    l2.append(int(input(f'Digite um valor para a coluna {e} da linha 2: ')))

print(l0)
print(l1)
print(l2)