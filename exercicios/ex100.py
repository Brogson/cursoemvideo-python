from random import randint

def sorteia(val):
    for c in range(0, 5):
        n = randint(1, 10)
        val.append(n)

def somaPar(val):
    s = 0
    for num in val:
        if num % 2 == 0:
            s += num
    print(f'A soma dos números pares da lista resulta: {s}')


# Programa Principal
valores = list()
sorteia(valores)
print(f'Os valores sorteados foram: {valores}')
somaPar(valores)
