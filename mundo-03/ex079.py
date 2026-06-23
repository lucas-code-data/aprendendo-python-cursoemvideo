"""Exercício Python #079 - Valores únicos em uma Lista"""

lista_valores = []
while True:
    valores = int(input('Digite um valor: '))
    if valores not in lista_valores:
        print('Valor adicionado com sucesso!')
        lista_valores.append(valores)
    else:
        print('Valor duplicado, não adicionarei!')
    continuacao = ' '
    while continuacao not in 'SN':
        continuacao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuacao == 'N':
        break
lista_valores.sort()
print(lista_valores)
