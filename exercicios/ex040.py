n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('REPROVADO! Sua média foi de {}'.format(media))
elif 5 <= media < 7:
    print('RECUPERAÇÃO! Sua média foi de {}'.format(media))
else:
    print('APROVADO! Sua média foi de {}'.format(media))
