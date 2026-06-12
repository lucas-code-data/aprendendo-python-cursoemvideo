"""Exercício Python #070 - Estatísticas em produtos"""

total_compra = valor_maior1000 = menor_valor = cont = 0
menor_produto = ' '
print('-'*40)
print(f'{"LOJAS ROSITOS":^40}')
print('-'*40)
while True:
    cont += 1
    produto = str(input('Nome do produto: ')).strip()
    valor = float(input('Preço do produto: R$'))
    total_compra += valor
    if valor > 1000:
        valor_maior1000 += 1
    if cont == 1:
        menor_valor = valor
        menor_produto = produto
    else:
        if valor < menor_valor:
            menor_valor = valor
            menor_produto = produto
    continuacao = ' '
    while continuacao not in 'SN':
        continuacao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuacao == 'N':
        print('---------- LOJA ENCERRADA POR HOJE ----------')
        break
print(f'''O total da compra foi R${total_compra:.2f}!
Temos {valor_maior1000} produto/produtos custando mais de R$1000.00!
O produto mais barato foi {menor_produto.lower()} que custou R${menor_valor:.2f}!''')
