"""Exercício Python #081 - Extraindo dados de uma Lista"""

lista_valores = []
while True:
    lista_valores.append(int(input('Digite um valor: ')))
    continuacao = ' '
    while continuacao not in 'SN':
        continuacao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuacao == 'N':
        break
print(f'Você digitou {len(lista_valores)} elementos na lista.')
lista_valores.sort(reverse = True)
print(f'Os valores da lista em ordem decrescente são {lista_valores}')
if 5 in lista_valores:
    print('O valor 5 está dentro da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
