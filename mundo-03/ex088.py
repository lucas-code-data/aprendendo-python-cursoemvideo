"""Exercício Python #088 - Palpites para a Mega Sena"""

from random import sample
from time import sleep
numeros_jogos = []

for num in range(1, 61):
    numeros_jogos.append(num)
print('-' * 34)
print(f'{'JOGO DA MEGA SENA':^34}')
print('-' * 34)
sorteamento = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{'-=' * 3}  SORTEANDO {sorteamento} JOGOS  {'-=' * 3}')
sleep(1)
for sort in range(0, sorteamento):
    print(f'Jogo {sort + 1}: {sorted(sample(numeros_jogos, 6))}')
    sleep(0.5)
print(f'{'-=' * 5} < BOA SORTE! > {'-=' * 5}')
