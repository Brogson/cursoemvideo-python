cadastro = list()
jogador = dict()
gols = list()
total = cont = 0
while True:
    nome = str(input('Nome: '))
    jogador['nome'] = nome
    partidas = int(input(f'Quantas partidas o {nome} jogou? '))
    jogador['Quantidade de Partidas'] = partidas
    for c in range(1, partidas+1):
        gol = int(input(f'Gols de {nome} na partida {c}: '))
        total += gol
        gols.append(gol)
    jogador['gols'] = gols[:]
    jogador['total'] = total
    cadastro.append(jogador.copy())
    gols.clear()
    jogador.clear()
    cont += 1
    total = 0
    continuar = str(input('Quer cadastrar mais um jogador? [S/N] ')).upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        continuar = str(input('Ocorreu um erro! Digite novamente: [S/N ]')).upper()

print('-'*30)
for c in range(0, cont):
    print(f'Código: {c}, Nome: {cadastro[c]['nome']}, Gols: {cadastro[c]['gols']}, Total: {cadastro[c]['total']}')
print('-'*30)
while True:
    dados = int(input('Mostrar dados de qual jogador? [999 para parar]'))
    if dados == 999:
        break
    print(f'Levantamento do jogador {cadastro[dados]['nome']}: ')
    for k in range(0, partidas):
        print(f'No jogo {k+1} fez {cadastro[dados]['gols'][k]} gols!')
print('Fim do programa!')
