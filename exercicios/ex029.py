v = int(input('Digite a velocidade de um carro em Km/h: '))
if v > 80:
    print('Você foi multado!')
    a = (v - 80)
    m = a * 7
    print('Você ultrapassou {}Km/h da velocidade máxima permitida!'.format(a))
    print('Logo, sua multa valerá R${:.2f}'.format(m))
else:
    print('{}Km/h está dentro das normas de trânsito! Boa viagem!'.format(v))
