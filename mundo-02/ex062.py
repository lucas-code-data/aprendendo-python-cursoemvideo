"""Exercício Python #062 - Super Progressão Aritmética v3.0"""

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
mais_termos = 10
total_termos = 0
while mais_termos != 0:
    cont = 1
    while cont <= mais_termos:
        print(termo, end=' -> ')
        termo += razao
        cont += 1
        total_termos += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total_termos} termos mostrados.')
