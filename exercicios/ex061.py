a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = 1
an = 0
print('Os 10 primeiros valores da PA são:')
while n <= 10:
    an = a1 + (n-1)*r
    print(an)
    n += 1
print("Fim do programa")
