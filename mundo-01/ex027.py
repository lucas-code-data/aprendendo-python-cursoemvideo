"""Exercício Python #027 - Primeiro e último nome de uma pessoa"""

nome_completo = input('Digite seu nome completo: ').strip().upper()
nomes = nome_completo.split()
print(f'''Muito prazer em te conhecer!
Seu primeiro nome é {nomes[0]}.
Seu último nome é {nomes[-1]}.''')