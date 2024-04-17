s = float(input('Digite seu salário: '))
if s <= 1250:
    print('Seu salário que antes valia R${:.2f} agora valerá R${:.2f}!'.format(s, s * 1.15))
else:
    print('Seu salário que antes valia R${:.2f} agora valerá R${:.2f}!'.format(s, s * 1.10))
