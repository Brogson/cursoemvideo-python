from datetime import date
nasc = int(input('Informe o seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc

if idade <= 9:
    print('O nadador se encontra na categoria MIRIM por ter {} anos de idade'.format(idade))
elif 9 < idade <= 14:
    print('O nadador se encontra na categoria INFANTIL por ter {} anos de idade'.format(idade))
elif 14 < idade <= 19:
    print('O nadador se encontra na categoria JUNIOR por ter {} anos de idade'.format(idade))
elif 19 < idade <= 20:
    print('O nadador se encontra na categoria SÊNIOR por ter {} anos de idade'.format(idade))
else:
    print('O nadador se encontra na categoria MASTER por ter {} anos de idade'.format(idade))
