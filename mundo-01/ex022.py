"""Exercício Python #022 - Analisador de Textos"""

nome = input('Digite seu nome completo: ').strip()
print(f'''Seu nome em maíusculo é: {nome.upper()}.
Seu nome em minúsculo é: {nome.lower()}.
Seu nome ao todo tem {len(nome) - nome.count(' ')} letras.
Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras.''')
