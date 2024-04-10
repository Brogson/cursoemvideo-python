money = float(input('Quantos reais você possui na carteira? '))
dolar = money // 3.27
resto = money % 3.27
print('Você pode comprar {} dólares com os {}  reais que possui! Na sua carteira restarão {:.2f} reais'.format(dolar, money, resto))
