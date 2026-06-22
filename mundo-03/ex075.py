"""Exercício Python #075 - Análise de dados em uma Tupla"""

numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')), 
           int(input('Digite o último número: ')))

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vez(es)')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado!')
print('Os valores pares digitados foram: ', end='')
for pares in numeros:
    if pares % 2 == 0:
        print(pares, end= ' ')
