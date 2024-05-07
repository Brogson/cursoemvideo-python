from time import sleep
print('Iniciando contagem regressiva para o lançamento!')
for c in range(10, 0, -1):
    sleep(1)
    print('{}!'.format(c))
sleep(1)
print('Lançado!!!')
