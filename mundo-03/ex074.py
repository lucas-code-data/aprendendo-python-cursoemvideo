"""Exercício Python #074 - Maior e menor valores em Tupla"""

from random import randint

valores_sorteados = (randint(0, 10), randint(0, 10), randint(0, 10),
                    randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for cont in valores_sorteados:
    print(cont, end=' ')
print(f'\nO maior valor sorteado foi: {max(valores_sorteados)}')
print(f'O menor valor sorteado foi: {min(valores_sorteados)}')
