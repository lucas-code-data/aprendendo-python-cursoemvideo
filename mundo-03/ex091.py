"""Exercício Python #091 - Jogo de Dados em Python"""

from random import randint
from operator import itemgetter
from time import sleep
cont = 1

sorteio = dict()

print('Valores sorteados:')
sleep(0.7)

# sorteio dos dados criando a chave 'jogador' dentro do dicionário e armazenando o valor sorteado
for jogador in range(1, 5):
    numero_aleatorio = randint(1, 6)
    print(f'Jogador{jogador} tirou {numero_aleatorio} no dado.')
    sorteio[f'jogador{jogador}'] = numero_aleatorio
    sleep(0.8)
print('-=' * 20)

print('  ==  RANKING DOS JOGADORES ==  ')
sleep(0.7)
# aqui eu organizo o dicionario e adiciono ele em uma nova variavel
# o sorted recebe o dicionário com chave e valor (função items)
# key da função sorted é diferente das keys do dicionário, significa aqui chave de busca
# depois com o itemggetter coloco somente o valor que é 1
# dai é organizado pelos valores e o reverse coloca em ordem do maior para menor
sorteio_organizado = sorted(sorteio.items(), key=itemgetter(1), reverse=True)

# exibição do sorteio organizado
for jogador in sorteio_organizado:
    print(f'{cont:>4}º Lugar: {jogador[0]} com {jogador[1]}.')
    sleep(0.8)
    cont += 1

"""OUTRA FORMA DE FAZER A EXIBIÇÃO É ÚTILIZANDO O ENUMERATE"""
# for indice, jogador in enumerate(sorteio_organizado):
#   print(f'{indice + 1:>4}º Lugar: {jogador[0]} com {jogador[1]}.')
