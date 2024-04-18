p = float(input('Digite o preço de um produto: '))
print('Digite a forma de pagamento:')
print('("0": À Vista no dinheiro, "1": À Vista no Cartão,\n "2": 2 vezes no Cartão e "3": 3 vezes ou mais o Cartão)')
x = int(input('Forma de pagamento: '))

if x == 0:
    novo = p * 0.9
    print('O seu produto que custava R${} agora custará R${} com 10% de desconto à vista no dinheiro!'.format(p, novo))
elif x == 1:
    novo = p * 0.95
    print('O seu produto que custava R${} agora custará R${} com 5% de desconto à vista no cartão!'.format(p, novo))
elif x == 2:
    print('O seu produto de R${} não recebe desconto!'.format(p))
else:
    novo = p * 1.20
    print('O produto de R${} teve aumento de 20% com os juros, custando agora R${}'.format(p, novo))
