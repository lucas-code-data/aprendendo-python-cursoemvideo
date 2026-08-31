"""Exercício Python #094 - Unindo dicionários e listas"""

pessoas = []
dados = {}
total_idade = media_idade = 0

while True:
    dados['nome'] = str(input('Nome: ')).strip().title()
    while True:
        dados['sexo'] = str(input('Sexo [M/F] ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas [M] ou [F].')
    dados['idade'] = int(input('Idade: '))
    while True:
        continuacao = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if continuacao in 'SN':
            break
        print('ERRO! Digite apenas [S] ou [N].')
    #pega os dicionários, cria um copia e coloca dentro da lista, após isso faz a limpeza do dicionário
    pessoas.append(dados.copy())
    dados.clear() #limpeza para receber novos dados, se o usuario não encerrar
    if continuacao == 'N':
        break
print('=' * 60)
#conta quantos dicionários tem dentro da lista, é o mesmo número de pessoas cadastradas
print(f'A) Ao todos temos {len(pessoas)} pessoas cadastradas.')
for pessoa in pessoas:
    total_idade += pessoa['idade']
media_idade = total_idade / len(pessoas)
print(f'B) A media de idade é de {media_idade} anos.')
print('C) As mulheres cadastradas foram ', end='')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=' ')
print('\nLista das pessoas que estão acima da média:')
#verificação de cada dicionário dentro da lista, fazendo exibição conforme a solicitação
for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        print(f'    Nome = {pessoa["nome"]}; sexo = {pessoa["sexo"]}; idade = {pessoa["idade"]}.')
print('<< ENCERRADO >>')
