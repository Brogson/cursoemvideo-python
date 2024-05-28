lista = list()
cadastro = dict()
mulheres = list()
totidade = cont = 0
mediamais = list()
while True:
    nome = str(input('Nome: '))
    cadastro['nome'] = nome
    idade = int(input('Idade: '))
    cadastro['idade'] = idade
    totidade += idade
    sexo = str(input('Sexo: [M/F] ')).upper()
    if sexo not in 'MF':
        sexo = str(input('Ocorreu um erro! Digite novamente: [M/F] ')).upper()
    cadastro['sexo'] = sexo
    if sexo == 'F':
        mulheres.append(cadastro.copy())
    lista.append(cadastro.copy())
    cadastro.clear()
    cont += 1
    continuar = str(input('Quer cadastrar mais alguem? [S/N] ')).upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        continuar = str(input('Ocorreu um erro! Digite novamente: [S/N] ')).upper()

media = totidade / cont
print('-=-' * 20)
print(f'Foram cadastradas {cont} pessoas!')
print('-=-' * 20)
print(f'A média de idade foi {media}')
print('-=-' * 20)
print('As mulheres cadastradas foram:')
for m in mulheres:
    print(m)
print('-=-' * 20)

for c in lista:
    if c['idade'] > media:
        mediamais.append(c.copy())

print(f'Pessoas com idade acima da média({media}):')
for i in mediamais:
    print(i)
