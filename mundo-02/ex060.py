"""Exercício Python #060 - Cálculo do Fatorial"""

from time import sleep
num = int(input('Digite um número para calcular seu Fatorial: '))
resultado = 1
cont = num
print('Calculando...')
sleep(1.5)
while cont > 0:
    print(cont, end = ' ')
    print('x' if cont > 1 else '=', end = ' ')
    resultado *= cont
    cont -= 1
print(resultado)
