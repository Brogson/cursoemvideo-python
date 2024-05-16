n = s = c = 0
while True:
    n = int(input('Digite um número: [999 para finalizar]'))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores digitados é {s}')
