total = 0
mil = 0
c = 1
menor = ''
menorv = 0
while True:
    print('Cadastro de novo produto')
    nome = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: '))
    total += valor
    if valor > 1000:
        mil += 1
    if c == 1:
        menor = nome
        menorv = valor
    if valor < menorv:
        menor = nome
        menorv = valor

    cont = str(input('Quer continuar cadatrando? [S/N]')).upper()
    if cont not in 'SN':
        cont = str(input('Houve um erro! Quer continuar cadatrando? [S/N]')).upper()
    if cont == 'N':
        break
print('Fim do programa!')
print(f'Foram cadastrados {total} reais em produtos!')
print(f'{mil} produtos cadastrados valem mais de 1000 reais')
print(f'O produto mais barato se chama {menor} com o valor de {menorv}')
