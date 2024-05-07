i = int(input('Digite um número de início: '))
f = int(input('Digite um número para o final: '))
p = int(input('Digite o passo em que a contagem será feita: '))
for c in range(i, f+1, p):
    print(c)
print('FIm!')
