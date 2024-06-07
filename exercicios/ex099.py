def maior(val):
    print(f'Os valores listados foram: {val}')
    print(f'Foram informados {len(val)} valores ao todo')
    val.sort(reverse=True)
    print(f'Entre os valores acima, o maior é: {val[0]}')


# Programa Principal
valores = list()
while True:
    while True:
        n = int(input('Digite um valor: '))
        valores.append(n)
        continuar = str(input('Quer adicionar mais um valor? [S/N] ')).upper()
        if continuar == 'N':
            break
        elif continuar != 'S':
            continuar = str(input('Ocorreu um erro! DIgite novamente: [S/N] ')).upper()
    maior(valores)
    valores.clear()
    repetir = str(input('Quer repetir a aplicação? [S/N] ')).upper()
    if repetir == 'N':
        break
    elif repetir != 'S':
        repetir = str(input('Ocorreu um erro! DIgite novamente: [S/N] ')).upper()
print('FIM DO PROGRAMA')
