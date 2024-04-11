alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
area = alt * larg
tinta = area / 2

print('A quantidade de tinta necessária para a sua parede de {}m² é {} litros'.format(area, tinta))
