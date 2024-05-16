from random import randrange
n = pc = s = v = 0
esc = ''
while True:
    n = int(input('Digite um valor de 0 a 10: '))
    esc = str(input('Escolha par ou ímpar: [P/I]')).upper()
    pc = randrange(0, 11)
    s = n + pc
    if s % 2 == 0 and esc == 'P':
        print(f'Você ganhou! {n} + {pc} = {s} e é par!')
    elif s % 2 == 1 and esc == 'I':
        print(f'Você ganhou! {n} + {pc} = {s} e é ímpar!')
    else:
        break
    v += 1
    esc = ''

if s % 2 == 0:
    esc = 'ímpar'
else:
    esc = 'par'
print(f'Você perdeu! {n} + {pc} = {s} e não é {esc}')
print(f'Teve uma sequência de {v} vitórias!')
