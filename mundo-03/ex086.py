"""Exercício Python #086 - Matriz em Python"""

lista_principal = [[], [], []] # cria 3 sublistas [0, 1 e 2] dentro da lista principal 

#os dois laços de repetição abaixo tem o mesmo resultado, apenas um consumindo mais linha do que o outro
"""LAÇOS ANINHADOS - um loop dentro do outro"""
for separacao in range(0, 3): # loop principal, para acessar cada sublista
    for indice in range(0, 3): # segundo loop, para adicionar os numeros numeros dentro das respectivas sublistas
        lista_principal[separacao].append(int(input(f'Digite um valor para [{separacao}, {indice}]: '))) 
print('-=' * 30)
"""LAÇOS SEQUÊNCIAIS - um loop em cada linha"""
for num in lista_principal[0]:
    print(f'[ {num:^3} ]', end='')
print()
for num in lista_principal[1]:
    print(f'[ {num:^3} ]', end='')
print()
for num in lista_principal[2]:
    print(f'[ {num:^3} ]', end='')
# 3 ultimos laços apenas para mostrar na tela a matriz 3 por 3, acessando os numeros de cada sublista
