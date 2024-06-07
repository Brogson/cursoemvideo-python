from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} ate {f} de {p} em {p}:')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=False)
            sleep(0.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=False)
            sleep(0.3)
            cont -= p
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))
