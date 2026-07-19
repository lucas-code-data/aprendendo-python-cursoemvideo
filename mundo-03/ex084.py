"""Exercício Python #084 - Lista composta e análise de dados"""

nome_peso = []
dados = []
peso = []
pessoas_mais_pesadas = []
pessoas_mais_leves = []
total_pessoas = 0

while True:
    nome_peso.append(str(input('Nome: ').strip()))
    nome_peso.append(float(input('peso: [KG] ')))
    total_pessoas += 1
    dados.append(nome_peso[:])
    nome_peso.clear()
    while True:
        continuacao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuacao in 'SN':
            break
    if continuacao == 'N':
        break
for kilo in dados:
    if kilo[1]:
        peso.append(kilo[1])
maior_peso = max(peso)
menor_peso = min(peso)
print(f'Ao todo, você cadastrou {total_pessoas} pessoas')
for pessoa in dados:
    if pessoa[1] == maior_peso:
        pessoas_mais_pesadas.append(pessoa[0])
    if pessoa[1] == menor_peso:
        pessoas_mais_leves.append(pessoa[0])
print(f'O maior peso foi de {maior_peso}KG. Peso de {pessoas_mais_pesadas}')
print(f'O menor peso foi de {menor_peso}KG. Peso de {pessoas_mais_leves}')
