from random import randrange
from time import sleep
print('Computador escolhendo um número de 0 a 5...')
n = randrange(0, 5)
chute = int(input('Qual o número que o computador pensou? '))
print('Processando...')
sleep(3)
if n == chute:
    print('Você acertou! Era o número {}'.format(n))
else:
    print('Você errou! O número correto era {}'.format(n))
