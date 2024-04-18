from time import sleep
n = int(input('Digite um numero inteiro qualquer: '))
print('Digite "1" para convertê-lo em binário, "2" para octal e "3" para hexadecimal')
conv = int(input('Digite para qual código quer converter seu número: '))

if conv == 1:
    print('Conversão para Binário!')
    print('Convertendo...')
    sleep(2)
    print(n, 'é igual a:', bin(n), sep='\t')
elif conv == 2:
    print('Conversão para Octal!')
    print('Convertendo...')
    sleep(2)
    print(n, 'é igual a:', oct(n), sep='\t')
else:
    print('Conversão para Hexadecimal!')
    print('Convertendo...')
    sleep(2)
    print(n, 'é igual a:', hex(n), sep='\t')

print('Fim da conversão!')
