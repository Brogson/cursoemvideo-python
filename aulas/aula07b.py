n1 = int(input('Digite um valor: '))
n2 = int(input('DIgite outro valor: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divInt = n1 // n2
resto = n1 % n2
poten = n1 ** n2
raiz = n1 ** (1/n2)

print('A soma é: {}'.format(soma))
print('A subtração é: {}'.format(sub))
print('A multiplicação é: {}'.format(mult))
print('A divisão é: {:.3f}'.format(div))
print('A divisão inteira é: {}'.format(divInt))
print('O resto é: {}'.format(resto))
print('A potência é: {}'.format(poten))
print('A radiciação é: {:.3F}'.format(raiz))

print('Para quebrar uma linha basta digitar \n e para não quebrar a linha de um print ', end=' >>> ')
print('Use contrabarra(n) e end=, respectivamente')