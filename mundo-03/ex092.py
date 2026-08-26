"""Exercício Python #092 - Cadastro de Trabalhador em Python"""

from datetime import date
ano_atual = date.today().year

dados = {}

#dicionário que altera de tamanho conforme as escolhas do usuario

dados['nome'] = str(input('Nome: ')).strip().title()
dados['nascimento'] = int(input('Ano de nascimento: '))
dados['carteira_trabalho'] = int(input('Carteira de trabalho: [0 não tem] '))

if dados.get('carteira_trabalho') != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))

print('=-' * 30)

dados['idade'] = ano_atual - dados.get('nascimento')
print(f'  - Nome tem o valor {dados.get('nome')}.')
print(f'  - Idade tem o valor {dados.get('idade')}.')
print(f'  - CTPS tem o valor {dados.get('carteira_trabalho')}.')

if dados.get('carteira_trabalho') != 0:
    print(f'  - Contratação tem o valor {dados.get('contratação')}.')
    print(f'  - Salário tem o valor R$ {dados.get('salario'):.2f}')
    ano_aposentadoria = dados.get('contratação') + 35
    dados['aposentadoria'] = idade_aposentadoria = ano_aposentadoria - dados.get('nascimento')
    print(f'  - Aposentadoria será com a idade no valor {dados.get('aposentadoria')}.')
print(dados)

"""PODERIA TER EXIBIDO OS DADOS COM UM FOR EM DADOS.ITEMS()"""
