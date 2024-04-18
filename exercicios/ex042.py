l1 = int(input('Digite um comprimento de reta em metros: '))
l2 = int(input('Digite outro comprimento de reta: '))
l3 = int(input('Digite o último segmento de reta em metros: '))

if l1 > (l2 - l3):
    if l1 < (l2 + l3):
        print('Os três lados ({}, {} e {}) formam um triângulo!'.format(l1, l2, l3))

        if l1 == l2 and l1 == l3:
            print('O seu triângulo é do tipo equilátero!')
        elif l1 == l2 or l1 == l3 or l2 == l3:
            print('O seu triângulo é do tipo isósceles!')
        else:
            print('O seu triângulo é do tipo escaleno!')
    else:
        print('Os três lados ({}, {} e {}) não formam um triângulo'.format(l1, l2, l3))
else:
    print('Os três lados ({}, {} e {}) não formam um triângulo'.format(l1, l2, l3))
