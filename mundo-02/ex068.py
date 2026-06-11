"""Exercício Python #068 - Jogo do Par ou Ímpar"""


from random import randint

cont_vitorias = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
while True:
    jogada_usuario = ' '
    jogada_comp = randint(1, 10)
    valor_usuario = int(input('Digite um valor: '))
    while jogada_usuario not in 'PI':
        jogada_usuario = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    resultado = valor_usuario + jogada_comp
    print(f'Você jogou {valor_usuario} e o computador {jogada_comp}. Total de {resultado} ', end='')
    if resultado % 2 == 0:
        print('DEU PAR!')
        resultado_jogadas = 'P'
    else:
        print('DEU IMPAR!')
        resultado_jogadas = 'I'
    if jogada_usuario == resultado_jogadas:
        print('''Você VENCEU!
VAMOS JOGAR NOVAMENTE...''')
        print('=-'*15)
        cont_vitorias += 1
    else:
        print('Você PERDEU!')
        print('=-'*15)
        break
print(f'GAME OVER! Você venceu {cont_vitorias} vez/vezes!')
