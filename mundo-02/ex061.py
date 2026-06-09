"""Exercício Python #061 - Progressão Aritmética v2.0"""

cont = 1
print(f'''GERADOR DE PA
{'==-'*10}''')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
while cont <= 10:
    print(termo, end = ' -> ')
    termo += razao
    cont += 1
print('Acabou')
