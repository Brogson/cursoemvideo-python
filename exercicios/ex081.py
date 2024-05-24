valores = []
c = 0
while True:
    valores.append(int(input('Digite um valor para adicionar')))
    c += 1
    continuar = str(input('Quer adicionar mais valores? [S/N]')).upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        continuar = str(input('Ocorreu um erro! Digite novamente: [S/N] '))
valores.sort(reverse=True)
print(f'Foram digitados {c} números.')
print(f'A lista ordenada é: {valores}')

if 5 in valores:
    print('O valor 5 foi digitado na lista')
else:
    print('O valor 5 não foi digitado na lista')
