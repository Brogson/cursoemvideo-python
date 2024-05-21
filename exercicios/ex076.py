pp = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 20.00, 'Transferidor', 4.25, 'Mochila', 120.32)
print('Listagem de Preços')
print('=-='*20)
for c in range(0, len(pp), 2):
    print(f'{pp[c]} R$ {pp[c+1]}')
