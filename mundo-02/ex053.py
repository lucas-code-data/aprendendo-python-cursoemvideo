"""Exercício Python #053 - Detector de Palíndromo"""

frase = ''.join(input('Digite uma frase: ').strip().upper().split())
frase_reversa = frase[::-1]
print(f'O inverso de {frase} é {frase_reversa}.')
if frase == frase_reversa:
    print('A frase digitada É UM PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALINDROMO!')
