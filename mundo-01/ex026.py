"""Exercício Python #026 - Primeira e última ocorrência de uma string"""

frase = input('Digite uma frase: ').strip().upper()
print(f'''A letra "A" aparece {frase.count('A')}.
A primeira letra "A" apareceu na posição {frase.find('A') + 1}.
A última letra "A" apareceu na posição {frase.rfind('A') + 1}''')
