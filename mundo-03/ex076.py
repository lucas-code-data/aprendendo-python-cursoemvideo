"""Exercício Python #076 - Lista de Preços com Tupla"""

lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
                     'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 
                     9.99, 'Mochila', 120.32, 'Canetas', 22.30,
                     'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for produtos in range(0, len(lista), 2):
    print(f'{lista[produtos]:.<31}R$ {lista[produtos + 1]:.2f}')
print('-' * 40)
