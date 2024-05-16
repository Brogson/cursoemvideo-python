sacar = int(input('Digite qual valor quer sacar: '))

cinquenta = sacar // 50
resto50 = sacar % 50
vinte = resto50 // 20
resto20 = resto50 % 20
dez = resto20 // 10
um = resto20 % 10

print(f'{cinquenta} notas de R$50.00, {vinte} notas de R$20.00, {dez} notas de R$10.00 e {um} moedas de R$1.00')
