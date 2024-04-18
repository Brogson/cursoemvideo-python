from datetime import date
nasc = int(input('Informe o seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
tempo = 18 - idade

if idade < 18:
    print('Você ainda tem {} anos! Ainda vai se alistar daqui a {} anos.'.format(idade, tempo))
elif idade == 18:
    print('Chegou o momento de se alistar. Parabéns pelos 18 anos!')
else:
    print('Você tem {} anos! Já deveria ter se alistado, pois se passaram {} anos!'.format(idade, tempo*-1))
