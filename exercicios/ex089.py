lista = []
nomes = []
notas = []
c = 0
while True:
    nomes.append(str(input('Nome: ')))
    notas.append(int(input('Nota 1: ')))
    notas.append(int(input('Nota 2: ')))
    nomes.append(notas[:])
    lista.append(nomes[:])
    notas.clear()
    nomes.clear()
    c += 1
    continuar = str(input('Deseja cadastrar mais alunos? [S/N] ')).upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        continuar = str(input('Ocorreu um erro! Digite novamente: [S/N] ')).upper()

for n in range(0, c):
    print(f'{n} - Aluno: {lista[n][0]} - Média: {(lista[n][1][0] + lista[n][1][1]) / 2}')
while True:
    aluno = int(input('Gostaria de ver as notas de qual aluno? Favor utilizar a numeração acima: [999 para finalizar]'))
    if aluno == 999:
        break
    else:
        print(f'0(a) aluno(a) {lista[aluno][0]} tirou as notas {lista[aluno][1][0]} e {lista[aluno][1][1]}')

print('Fim do processo!')
