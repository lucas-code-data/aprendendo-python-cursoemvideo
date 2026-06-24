"""Exercício Python #082 - Dividindo valores em várias listas"""

lista_valores = list()
while True:
    lista_valores.append(int(input('Digite um número: ')))
    print('=-' * 20)
    while True:
        continuacao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print('=-' * 20)
        if continuacao in 'SN':
            break
        else:
            print('ERRO! Digite apenas "S" ou "N"')
    if continuacao == 'N':
        break
print('=-' * 20)
print(f'A lista completa é: {lista_valores}')
lista_pares = []
lista_impares = []
for numero in lista_valores:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
print(f'A lista de pares é: {lista_pares}')
print(f'A lista de impares é: {lista_impares}')
