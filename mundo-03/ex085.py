"""Exercício Python #085 - Listas com pares e ímpares"""

lista_principal = [[], []]

for cont in range(1, 8):
    numero_usuario = int(input(f'Digite o {cont}º número: '))
    if numero_usuario % 2 == 0:
        lista_principal[0].append(numero_usuario)
    else:
        lista_principal[1].append(numero_usuario)
print('-=' * 20)
lista_principal[0].sort()
lista_principal[1].sort()
print(f'Os valores PARES foram: {lista_principal[0]}')
print(f'Os valores IMPARES foram: {lista_principal[1]}')
