def area(lar, comp):
    a = lar * comp
    print(f'A área de largura de {lar}m e comprimento de {comp}m possui área de {a}m².')


# Programa Principal:
area(int(input('Digite a largura do terreno: ')),
     int(input('Digite o comprimento do terreno: ')))
