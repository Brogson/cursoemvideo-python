n = int(input('Digite quantos números da sequência de fibonacci quer ver: '))
cont = 0
maisnovo = 1
novo = 1
velho = 0
while cont <= n:
    print(maisnovo)
    maisnovo = novo + velho
    velho = novo
    novo = maisnovo
    cont += 1
print('Fim do programa!')
