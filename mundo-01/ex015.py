"""Exercício Python #015 - Aluguel de Carros"""

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
total = 60 * dias + 0.15 * km
print(f'O total a pagar é de R${total:.2f}!')