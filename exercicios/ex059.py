menu = 4
while menu == 4:
    print('Bem-vindo relacionador de números, responda as perguntas abaixo')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print('[1] para somar')
    print('[2] para multiplicar')
    print('[3] para saber qual o maior')
    print('[4] para colocar novos números')
    print('[5] para sair do programa')
    menu = int(input('Digite o que quer fazer: '))
    if menu == 1:
        print('A soma entre {} e {} vale {}'.format(n1, n2, n1 + n2))
    if menu == 2:
        print('A multiplicação entre {} e {} vale {}'.format(n1, n2, n1 * n2))
    if menu == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n2))
    if menu == 4:
        print('Reiniciando o programa...')
    if menu == 5:
        print('Finalizando o programa...')
print('Fim do programa! Obrigado por participar!')
