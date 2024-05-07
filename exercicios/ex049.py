n = int(input('Digite o número ao qual você quer saber a tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
print('Fim da tabuada do {}!'.format(n))
