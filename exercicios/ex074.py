from random import sample

num = tuple(sample(range(10), 5))
print(f'Os números gerados foram {num}')
num = sorted(num)
print(f'O menor valor da tupla é {num[0]}')
print(f'O maior valor da tupla é {num[4]}')
