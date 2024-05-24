valores = []
while True:
    n = int(input('Digite um valor para adicionar: '))
    if n in valores:
        print('O valor já foi digitado antes')
    else:
        valores.append(n)
    continuar = str(input('Gostaria de adicionar mais um valor? [S/N]')).upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        continuar = str(input('Ocorreu um erro, responda novamente: [S/N]')).upper()
valores.sort()
print(f'A os valores digitados, em ordem crescente são: {valores}')
