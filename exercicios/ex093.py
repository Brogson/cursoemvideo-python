jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input('Quantidade de partidas jogadas: '))
jogador['quantidade de partidas'] = partidas
for c in range(1, partidas+1):
    gol = int(input(f'Gols feitos na partida {c}: '))
    gols.append(gol)
    total += gol

jogador['gols'] = gols
jogador['Total de gols'] = total
print('-=-' * 20)
print(jogador)
print('-=-' * 20)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 20)

print(f'O jogador {jogador['nome']} jogou {partidas} partidas:')
for i, j in enumerate(gols):
    print(f'Na partida {i+1} fez {j} gols.')
print(f'Foi um total de {total} gols')
