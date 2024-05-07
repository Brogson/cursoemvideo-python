a1 = int(input('Digite o primeiro termo: '))
r = int(input('Qual será a razão da progressão? '))
for c in range(1, 11):
    t = a1 + (c - 1)*r
    print(t)
print('Fim da operação!')
