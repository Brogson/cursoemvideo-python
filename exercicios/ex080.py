valores = [999999]
for cont in range(0, 5):
    n = int(input('Digite um valor para adicionar: '))
    if n <= valores[0]:
        valores.insert(0, n)
    elif n <= valores[1]:
        valores.insert(1, n)
    elif n <= valores[2]:
        valores.insert(2, n)
    elif n <= valores[3]:
        valores.insert(3, n)
    else:
        valores.insert(4, n)
valores.pop()
print(f'A lista ordenada é: {valores}')
