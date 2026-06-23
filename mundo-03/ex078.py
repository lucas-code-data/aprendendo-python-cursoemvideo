"""Exercício Python #078 - Maior e Menor valores na Lista"""

valores = []
print('=-' * 20)
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-' * 20)
maior_valor = max(valores)
menor_valor = min(valores)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior_valor} nas posições ' ,end='')
for pos, valor in enumerate(valores):
    if valor == maior_valor:
        print(pos, end='...')
print(f'\nO menor valor digitado foi {menor_valor} na posições ', end='')
for pos, valor in enumerate(valores):
    if valor == menor_valor:
        print(pos, end='...')
