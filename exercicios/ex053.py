from unidecode import unidecode
s = 0
frase = str(input('Digite uma frase: '))
frase = frase.lower()
frase = frase.replace(" ", "")
frase = unidecode(frase)
tamanho = len(frase) - 1
for c in range(0, len(frase)):
    if frase[c] == frase[tamanho-c]:
        s = 1
    else:
        s = 2
if s == 1:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
