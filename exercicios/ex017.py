from math import hypot
a = int(input('Digite um valor para o cateto A: '))
b = int(input('Digite um valor para o cateto B: '))
hip = hypot(a, b)
print('O triângulo retângulo com catetos de valores {} e {} possui hipotenusa {}'.format(a, b, hip))
