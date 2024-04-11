alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
area = alt * larg
tinta = area / 2
print('Sua parede tem uma dimensão de {}x{} e sua área é de {}m²'.format(alt, larg, area))
print('A quantidade de tinta necessária para a sua parede de {}m² é {} litros'.format(area, tinta))
