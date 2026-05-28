"""Exercício Python #013 - Reajuste Salarial"""

salario = float(input('Qual é o salário do funcionário? R$'))
novo_salario = salario * 0.15
print(f'Um funcionário que ganhava R${salario:.2f}, com o aumento de 15%, passará a receber {salario + novo_salario:.2f}!')