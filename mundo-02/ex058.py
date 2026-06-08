"""Exercício Python #058 - Jogo da Adivinhação v2.0"""

from random import randint
escolha_comp = randint(0, 10)
palpite = None
tentativas = 0

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
while not palpite == escolha_comp:
    palpite = int(input('Qual é seu palpite?'))
    if palpite < escolha_comp:
        print('Mais... Tente mais uma vez!')
    elif palpite > escolha_comp:
        print('Menos... Tente mais uma vez!')
    tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns!')
