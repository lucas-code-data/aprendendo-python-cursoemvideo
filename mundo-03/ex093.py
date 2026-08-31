"""Exercício Python #093 - Cadastro de Jogador de Futebol"""

dados = dict()
gols_por_partida = []

dados['nome'] = str(input('Nome do jogador: ')).strip().title()
dados['partidas'] = int(input(f'Quantas partidas {dados['nome']} jogou? '))

#crio uma lista com os gols p/partida e depois adiciono dentro do dicionário
for cont in range(1, dados['partidas'] + 1):
    gols_por_partida.append(int(input(f'   Quantos gols na partida {cont}? ')))
dados['gols'] = gols_por_partida[:]
dados['total_gols'] = sum(dados['gols']) #soma dos gols
print('=' * 90)
print(dados)
print('=' * 90)

# !!! aqui eu poderia ter usado um for com dados.items para acessar cada chave e seus valores
print(f'O campo nome tem o valor: {dados['nome']}')
print(f'O campo gols tem o/os valor/valores: {dados['gols']}')
print(f'O campo total de gols tem o valor: {dados['total_gols']}')
print('=' * 90)

print(f'O jogador {dados['nome']} jogou {dados['partidas']} partidas.')

# !!! aqui eu poderia ter usado um for indice, valor in enumerate(dados['gols'])
for jogo in range(0, dados['partidas']):
    print(f'   => Na partida {jogo + 1} , fez {dados['gols'][jogo]} gols.')
