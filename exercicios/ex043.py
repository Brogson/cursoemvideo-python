peso = float(input('Digite o seu peso em Kg: '))
alt = float(input('Digite sua altura em metros: '))
imc = peso/alt**2

if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no seu peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está na obesidade!')
else:
    print('Cuidado, você está em Obesidade Mórbida!')
