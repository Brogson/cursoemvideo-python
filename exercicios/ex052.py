s = 0
n = int(input('Digite um valor para saber se é primo: '))
for c in range(2, n):
    if n % c == 0:
        s = 1
if s == 1:
    print('O número não é primo!')
else:
    print('O número é primo!')
print('Fim da operação')
