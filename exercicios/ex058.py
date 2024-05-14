import random
from time import sleep
cont = 1
print('A máquina irá sortear um número de 0 a 10!')
sleep(2)
n = random.randrange(1, 11)
print('Pensou!')
sleep(1)
p = int(input('Digite qual número acha que a máquina pensou: '))
while p != n:
    p = int(input('Errou, tente novamente até acertar: '))
    cont += 1
print('Você acertou! O número pensado era {}'.format(n))
print('Você precisou de {} tentativas!'.format(cont))
