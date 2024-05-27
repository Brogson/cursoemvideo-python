from random import randint
result = dict()
result['J1'] = randint(1, 7)
result['J2'] = randint(1, 7)
result['J3'] = randint(1, 7)
result['J4'] = randint(1, 7)
c = 4

for k, v in result.items():
    print(f'O jogador {k} tirou {v}')

ordenado = sorted(result)

for p, r in ordenado:
    print(f'{c}º lugar: {p} com {r} pontos')
    c -= 1