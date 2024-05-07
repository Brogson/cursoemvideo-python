n = 0
for c in range(3, 500, 3):
    if c % 2 == 1:
        n += c
print('A soma dos números ímpares múltiplos de 3 é: {}'.format(n))
