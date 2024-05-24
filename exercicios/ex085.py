num = [[], []]
n = 0
for c in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Todos os valores: {num}')
