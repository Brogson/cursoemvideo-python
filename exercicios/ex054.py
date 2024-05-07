from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    p = int(input('Digite o ano de nascimento: '))
    if date.today().year - p >= 18:
        maior += 1
    else:
        menor += 1
print('Quantidade de pessoas na maioridade: {}'.format(maior))
print('Quantidade de pessoas menores de idade: {}'.format(menor))
