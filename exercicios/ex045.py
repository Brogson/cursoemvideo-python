from random import randrange
from time import sleep
print('Vamos jogar Jokempô?')
print('Vou decidir o que vou jogar primeiro...')
sleep(1.5)
pc = randrange(1, 4)
print('1 para Pedra, 2 para Papel e 3 para Tesoura, ok?')
eu = int(input('O que vai jogar? '))

if pc == eu:
    print('Jogo empatado!')
elif pc == 1:
    if eu == 2:
        print('Você ganhou! Papel ganha de pedra!')
    elif eu == 3:
        print('Você perdeu! Tesoura perde para pedra!')
elif pc == 2:
    if eu == 1:
        print('Você perdeu! Pedra perde para papel!')
    elif eu == 3:
        print('Você ganhou! Tesoura ganha de Papel!')
else:
    if eu == 1:
        print('Você ganhou! Pedra ganha de tesoura!')
    elif eu == 3:
        print('Você perdeu! Papel perde para Tesoura!')
