"""Exercício Python #048 - Soma ímpares múltiplos de três"""

soma = total_valores = 0
for c in range(3, 501, 6):
    soma += c
    total_valores += 1
print(f'A soma de todos os {total_valores} valores solicitados é {soma}!')