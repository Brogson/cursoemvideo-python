valores = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor para adicioná-lo à lista: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = str(input('Quer adicionar mais valores? [S/N]')).upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        continuar = str(input('Ocorreu um erro! Digite novamente: [S/N] '))
print(f'A lista completa é: {valores}')
print(f'Os valores digitados pares são: {pares}')
print(f'OS valores ímpares digitados são: {impares}')
