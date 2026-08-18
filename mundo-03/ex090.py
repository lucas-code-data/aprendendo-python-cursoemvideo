"""Exercício Python #090 - Dicionário em Python"""

boletim = dict() # cria um dicionário

# adiciona as chaves 'nome' e 'media' dentro do dicionário e armazena os valores respectivamente
boletim['nome'] = str(input('Nome: ')).strip().title()
boletim['media'] = float(input(f'Média de {boletim["nome"]}: '))

# cria uma nova chave 'situacao' e motra a condição do aluno com base na média
if boletim['media'] >= 7:
    boletim['situacao'] = 'Aprovado'
elif boletim['media'] >= 5:
    boletim['situacao'] = 'Recuperação'
else:
    boletim['situacao'] = 'Reprovado' 

# exibição dos dados na tela
print('-=' * 15)
print(f'''  - Nome é igual a {boletim["nome"]}.
  - Média é igual a {boletim["media"]:.1f}
  - Situação é igual a {boletim["situacao"]}''')

"""CASO EU QUISESSE EXIBIR OS DADOS COM UM LAÇO"""
#for keys, values in boletim.items():
#    print(f'{keys} é igual a {values}')
