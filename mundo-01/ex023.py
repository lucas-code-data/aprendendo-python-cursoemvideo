"""Exercício Python #023 - Separando dígitos de um número"""

num = int(input('Informe um número: '))
print(f'''Analisando o número...
Unidade: {num // 1 % 10}.
Dezena: {num // 10 % 10}.
Centena: {num // 100 % 10}.
Milhar: {num // 1000 % 10}.''')