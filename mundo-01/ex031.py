"""Exercício Python #031 - Custo da Viagem"""

distancia = float(input('Qual é a distância da sua viagem? KM'))
print(f'Você está prestes a começar uma viagem de {distancia:.2f}KM.')
if distancia <= 200:
    preco_viagem = distancia * 0.50
    print(f'O preço da sua viagem ficará R${preco_viagem:.2f}!')
else:
    preco_viagem = distancia * 0.45
    print(f'O preço da sua viagem ficará em R${preco_viagem:.2f}!')
print('Desejo uma ótima viagem!')
