n1 = float(input('Digite um número qualquer: '))
n2 = float(input('Digite outro número qualquer: '))
n3 = float(input('Digite um último número qualquer: '))
if n1 > n2:
    if n1 > n3:
        print('O {} é o maior número!'.format(n1))
    else:
        print('O {} é o maior número!'.format(n3))
else:
    if n2 > n3:
        print('O {} é o maior número!'.format(n2))
    else:
        print('O {} é o maior número!'.format(n3))

if n1 < n2:
    if n1 < n3:
        print('O {} é o menor número!'.format(n1))
    else:
        print('O {} é o menor número!'.format(n3))
else:
    if n2 < n3:
        print('O {} é o menor número!'.format(n2))
    else:
        print('O {} é o menor número!'.format(n3))
