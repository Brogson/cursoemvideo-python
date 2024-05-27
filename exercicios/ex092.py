from datetime import datetime
info = dict()
nome = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
clt = int(input('Carteira de Trabalho: '))
info['nome'] = nome
info['nascimento'] = nasc
idade = datetime.now().year - nasc
info['idade'] = idade
info['CTPS'] = clt
if clt != 0:
    contrato = int(input('Ano de contratação: '))
    info['Ano de contrato'] = contrato
    anoaposent = contrato + 35
    info['salário'] = float(input('Salário atual: '))
    aposent = anoaposent - datetime.now().year + idade
    info['Idade de Aposentado'] = aposent

print(f'{info['nome']}, de {idade} anos,  irá se aposentar com {info['Idade de Aposentado']}')
print(info)
