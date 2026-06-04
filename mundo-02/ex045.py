"""Exercício Python #045 - GAME: Pedra Papel e Tesoura"""

from time import sleep
from random import randint

escolha_comp = randint(0, 2)
if escolha_comp == 0:
    escolha_comp = 'PEDRA'
elif escolha_comp == 1:
    escolha_comp = 'PAPEL'
else:
    escolha_comp = 'TESOURA'
print(f'''{'-='*20}\n{'VAMOS JOGAR JOKENPO':^40}\n{'-='*20}
Opções do jogador:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA''')
escolha_jogador = int(input('Qual é a sua jogada? '))
if escolha_jogador in (0, 1, 2):
    if escolha_jogador == 0:
        escolha_jogador = 'PEDRA'
    elif escolha_jogador == 1:
        escolha_jogador = 'PAPEL'
    else:
        escolha_jogador = 'TESOURA'
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print(f'''{'-='*20}
Computador jogou {escolha_comp}
Jogador jogou {escolha_jogador}
{'-='*20}''')
    if escolha_comp == escolha_jogador:
        print('EMPATE')
    elif(
        escolha_comp == 'PAPEL' and escolha_jogador == 'PEDRA'
        or escolha_comp == 'PEDRA' and escolha_jogador == 'TESOURA'
        or escolha_comp == 'TESOURA' and escolha_jogador == 'PAPEL'
    ):    
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADOR VENCEU')
else:
     print('JOGADA INVÁLIDA!')
