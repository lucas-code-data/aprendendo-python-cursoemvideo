"""Exercício Python #073 - Tuplas com Times de Futebol"""

classificacao = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR',
                 'Bragantino', 'Bahia', 'Coritiba', 'São Paulo',
                 'Athletico-MG', 'Corinthians', 'Cruzeiro', 'Botafogo', 
                 'EC Vitoria', 'Internacional', 'Santos', 'Gremio', 
                 'Vasco da Gama', 'Remo', 'Mirassol', 'Chapecoense')

print('-=' * 30)
print(f'Lista de times do brasileirão: {classificacao}')
print('-=' * 30)
print(f'Os 5 primeiros são: {classificacao[0:5]}')
print('-=' * 30)
print(f'Os últimos 4 são: {classificacao[16:]}')
print('-=' * 30)
print(f'Times em ordem alfábetica: {sorted(classificacao)}')
print('-=' * 30)
print(f'A chapecoense está na {classificacao.index("Chapecoense") + 1}º posição')
