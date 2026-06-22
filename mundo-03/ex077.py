"""Exercício Python #077 - Contando vogais em Tupla"""

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYHTON', 
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for itens in palavras:
    print(f'\nNa palavra {itens} temos ', end='')
    for letras in itens:
        if letras in 'AEIOU':
            print(letras, end=' ')
