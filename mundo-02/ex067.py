"""Exercício Python #067 - Tabuada v3.0"""

from time import sleep
while True:
    valor = int(input('Quer ver a tabuada de qual valor? [numero negativo para encerrar] '))
    print('==-'*20)
    if valor < 0:
        print('Encerrando...')
        sleep(1)
        break
    for cont in range(1, 11):
        resultado = valor * cont
        print(f'{valor} x {cont:2} = {resultado}')
    print('==-'*20)
print('Programa tabuada encerrado com sucesso!')
print('==-'*20)
