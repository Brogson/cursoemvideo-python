lista = list()
dados = list()
cont = 0
totalkg = 0
pesados = list()
leves = list()
maiorpeso = menorpeso = 0
Nmaiorpeso = Nmenorpeso = ''
while True:
    nome = str(input('Nome: ')).title()
    dados.append(nome)
    peso = float(input('Peso: '))
    dados.append(peso)
    lista.append(dados[:])
    dados.clear()
    print('Dados cadastrados!')
    if cont == 0:
        maiorpeso = peso
        Nmaiorpeso = nome
        menorpeso = peso
        Nmenorpeso = nome
    else:
        if peso > maiorpeso:
            maiorpeso = peso
            Nmaiorpeso = nome
        if peso < menorpeso:
            menorpeso = peso
            Nmenorpeso = nome
    cont += 1
    continuar = str(input('Quer cadastrar mais alguém? [S/N] ')).upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        continuar = str(input('Ocorreu um erro! Digite novamente [S/N] '))
print(f'Foram cadastradas {cont} pessoas!')

for c in range(0, len(lista)):
    totalkg += lista[c][1]

media = totalkg/len(lista)
for p in range(0, len(lista)):
    if lista[p][1] <= media:
        leves.append(lista[p][0])
    else:
        pesados.append(lista[p][0])
print(f'As pessoas mais leves são: {leves}')
print(f'As pessoas mais pesadas são: {pesados}')
print(f'A pessoa mais leve é {Nmenorpeso} com {menorpeso} Kg')
print(f'A pessoa mais pesada é {Nmaiorpeso} com {maiorpeso}kg ')
