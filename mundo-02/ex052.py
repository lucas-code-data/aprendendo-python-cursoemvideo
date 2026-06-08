"""Exercício Python #052 - Números primos"""

cont_div = 0
num = int(input('Digite um número inteiro: '))
for cont in range(1, num + 1):
    if num % cont == 0:
        print('\033[34m', end= '')
        cont_div += 1
    else:
        print('\033[m', end= '')
    print(cont, end= ' ')
print(f'\n\033[mO número {num} é divisível {cont_div} vezes.')
if cont_div == 2:
    print('Por isso ele É UM NÚMERO PRIMO!')
else:
    print('Por isso ele NÃO É UM NÚMERO PRIMO!')