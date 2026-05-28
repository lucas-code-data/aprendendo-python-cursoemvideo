"""Exercício Python #036 - Aprovando Empréstimo"""

valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valor / (12 * anos)
porcentagem_salario = salario * 0.30

print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}!')
if prestacao > porcentagem_salario:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
