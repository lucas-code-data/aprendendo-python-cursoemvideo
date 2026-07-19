"""Exercício Python #083 - Validando expressões matemáticas"""

expressao = str(input('Digite a expressão matemática: '))
saldo = 0

for caracter in expressao:
    if caracter == '(':
        saldo += 1
    elif caracter == ')':
        saldo -= 1
    
    if saldo < 0:
        break

if saldo == 0:
    print('Sua expressão está CORRETA!')
else:
    print('Sua expressão está inválida!')
