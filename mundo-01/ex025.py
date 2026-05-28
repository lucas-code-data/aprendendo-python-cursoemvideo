"""Exercício Python #025 - Procurando uma string dentro de outra"""

nome = input('Qual é o seu nome completo? ').strip().upper()
print(f'Seu nome tem Silva? {'SILVA' in nome}')
