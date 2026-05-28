'''Exercício Python #028 - Jogo da Adivinhação v.1.0'''

from random import randint
from time import sleep

escolha_comp = randint(0, 5)
print(f'''{'-=' * 40}
{'Vou pensar em um número entre 0 e 5. Tente adivinhar...'}
{'-=' * 40}''')
escolha_jog = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if escolha_jog == escolha_comp:
    print('VOCÊ GANHOU! Parabens.')
else:
    print(f'GANHEI! Eu pensei no número {escolha_comp} e não no número {escolha_jog}.')
