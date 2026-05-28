"""Exercício Python #010 - Conversor de Moedas"""

dinheiro = float(input('Quanto de dinheiro você possui na sua carteira? R$'))
dolar = float(input('Qual o valor do dólar atualmente? US$'))
print(f'Com R${dinheiro:.2f} você pode comprar US${dinheiro / dolar:.2f}')