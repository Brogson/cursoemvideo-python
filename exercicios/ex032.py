from datetime import date
ano = int(input('Digite um ano qualquer (Digite 0 para o ano atual): '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} foi/será bissexto!'.format(ano))
else:
    print('O ano {} não foi/será bissexto!'.format(ano))
