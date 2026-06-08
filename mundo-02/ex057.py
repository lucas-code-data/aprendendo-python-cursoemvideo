"""Exercício Python #057 - Validação de Dados"""

sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: [M/F] ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
