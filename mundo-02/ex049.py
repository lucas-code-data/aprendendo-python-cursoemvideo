"""Exercício Python #049 - Tabuada v.2.0"""

num = int(input('Digite um número para ver sua tabuada: '))
print('-='*20)
for c in range(1, 11):
    print(f'{num} x {c:2} = {num * c}')
print('-='*20)
