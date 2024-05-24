valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

novo = list(valores[:])
novo.sort()
menor = novo[0]
posMenor = valores.index(menor)

novo.sort(reverse=True)
maior = novo[0]
posMaior = valores.index(maior)

print(f'O menor valor é {menor}, na posição {posMenor}.')
print(f'O maior valor é {maior}, na posição {posMaior}.')
