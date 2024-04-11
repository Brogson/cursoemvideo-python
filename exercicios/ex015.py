km = float(input('Digite a quantidade de Km que seu carro percorreu: '))
dias = int(input('Informe quantos dias o carro esteve em sua posse: '))
valor = (0.15 * km) + (60 * dias)
print('O valor total a se pagar pelo aluguel do carro é: R${:.2f}'.format(valor))
