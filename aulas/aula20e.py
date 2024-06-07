def dobra(val):
    print('Duplicando valores...')
    for v, p in enumerate(val):
        valores[v] = p * 2


# Programa Principal
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
