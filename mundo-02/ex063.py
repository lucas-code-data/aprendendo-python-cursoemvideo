"""Exercício Python #063 - Sequência de Fibonacci v1.0"""

print('-'*20)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*20)
termos = int(input('Quantos termos você quer mostrar? '))
seq1 = seq3 = 0 
seq2 = 1
cont = 1
while cont <= termos:
    seq3 = seq1 + seq2
    print(seq1, end=' -> ')
    seq1 = seq2
    seq2 = seq3
    cont += 1
print('FIM')
