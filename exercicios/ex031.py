d = int(input('Digite a distância de uma viagem em Km: '))
if d <= 200:
    p = d * 0.5
    print('O valor da passagem para {}Km será R${}!'.format(d, p))
else:
    p = d * 0.45
    print('O valor da passagem para {}Km será R${}!'.format(d, p))
