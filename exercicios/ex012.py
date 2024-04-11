prod = float(input('Digite o preço de seu produto: '))
desc = prod * 0.05
preco = prod - desc
print('Seu produto que antes valia R${} teve 5% de desconto: R${}.'.format(prod, desc))
print('Agora custará com desconto R${}!'.format(preco))