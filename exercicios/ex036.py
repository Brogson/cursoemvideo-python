casa = float(input('Digite o valor da casa em questão: '))
sal = float(input('Qual o seu salário? '))
ano = int(input('Em quantos anos pretende pagar o empréstimo? '))

prest = casa / (12*ano)

if prest > 0.3 * sal:
    print('O seu empréstimo foi negado!')
    print('O valor de R${:.2f} da casa não pode ser financiado em apenas {} ano(s)'.format(casa, ano))
else:
    print('Você poderá realizar o empréstimo tranquilamente!')
    print('A parcela mensal valerá R${:.2f} a ser paga durante {} meses.'.format(prest, 12*ano))
