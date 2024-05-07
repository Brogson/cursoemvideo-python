soma = 0
media = 0
maioridadeM = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('-----{}ª Pessoa-----'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO: (M ou F)')).strip()

    soma += idade
    if p == 1 and sexo in 'Mm':
        maioridadeM = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeM:
        maioridadeM = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media = soma/4
print('A média das idades é: {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadeM, nomevelho))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(totmulher20))