from random import randint
lista = list()
d = 0
n = 0
q = int(input('Quantos jogos quer sortear? '))
print(f'Sorteando {q} jogos...')
for c in range(1, q+1):
    while True:
        n = randint(1, 61)
        if d == 0:
            lista.append(n)
        else:
            if n not in lista:
                lista.append(n)
            if len(lista) == 6:
                break
        d += 1
    print(f'Jogo {c}: {lista}')
    lista.clear()
