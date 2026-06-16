"""Exercício Python #071 - Simulador de Caixa Eletrônico"""

print('=' * 40)
print(f"{'BANCO ROSITOS':^40}")
print('=' * 40)
cedulas_cinquenta = cedulas_vinte = cedulas_dez = cedulas_cinco = cedulas_um = 0
while True:
    valor_sacado = int(input('Qual valor você quer sacar? R$'))
    while valor_sacado >= 50:
        cedulas_cinquenta += 1
        valor_sacado -= 50
    if cedulas_cinquenta >= 1:
        print(f'Total de {cedulas_cinquenta} cedulas de R$50!')
    while valor_sacado >= 20:
        cedulas_vinte += 1
        valor_sacado -= 20
    if cedulas_vinte >= 1:
        print(f'Total de {cedulas_vinte} cedulas de R$20!')
    while valor_sacado >= 10:
        cedulas_dez += 1
        valor_sacado -= 10
    if cedulas_dez >= 1:
        print(f'Total de {cedulas_dez} cedulas de R$10!')
    while valor_sacado >= 5:
        cedulas_cinco += 1
        valor_sacado -= 5
    if cedulas_cinco >= 1:
        print(f'Total de {cedulas_cinco} cedulas de R$5!')
    while valor_sacado >= 1:
        cedulas_um += 1
        valor_sacado -= 1
    if cedulas_um >= 1:
        print(f'Total de {cedulas_um} cedulas de R$1!')
    print('='*40)
    print('VOLTE SEMPRE AO BANCO ROSITOS, TENHA UM BOM DIA!!!')
    break 
