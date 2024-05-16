cont = 'S'
maior = 0
homem = 0
Fmenor20 = 0
while cont == 'S':
    print('CADASTRO')
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [M/F]: ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Ocorreu um erro, digite o sexo novamente: [M/F]')).upper()
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        Fmenor20 += 1
    cont = str(input('Quer cadastrar mais? [S/N]')).upper()

print(f'Cadastraram-se {maior} pessoas com mais de 18 anos, {homem} homens e {Fmenor20} mulheres com menos de 20 anos.')
