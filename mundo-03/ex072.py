"""Exercício Python #072 - Número por Extenso"""

numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                   'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 
                   'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
                   'dezoito', 'dezenove', 'vinte')

while True:
    numero_usuario = int(input('Digite um número entre 0 e 20: '))
    print('-=' * 20)
    while numero_usuario not in range(0, 21):
        numero_usuario = int(input('Tente novamente. Por favor, digite um número entre 0 e 20: '))
        print('-=' * 20)
    print(f'Você digitou o número {numeros_extenso[numero_usuario]}!')
    print('-=' * 20)
    continuacao = ' '
    while continuacao not in 'SN':
        continuacao = str(input('Deseja continuar? ')).upper().strip()[0]
    print('-=' * 20)
    if continuacao == 'N':
        print('Programa encerrado!')
        break
