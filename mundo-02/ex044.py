"""Exercício Python #044 - Gerenciador de Pagamentos"""

print('========== LOJAS ROSITO ==========')
preco_compra = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] Á vista dinheiro/pix
[ 2 ] Á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
forma_pagamento = int(input('Qual a forma de pagamento? '))
if forma_pagamento == 1:
    desconto10 = preco_compra * 0.10
    print(f'Sua compra de {preco_compra:.2f} vai custar {preco_compra - desconto10:.2f} no final.')
elif forma_pagamento == 2:
    desconto5 = preco_compra *0.05
    print(f'Sua compra de {preco_compra:.2f} vai custar {preco_compra - desconto5:.2f} no final.')
elif forma_pagamento == 3:
    print(f'''Sua compra será parcelada no cartão em 2x de {preco_compra / 2:.2f} SEM JUROS.
Com o valor total da compra em {preco_compra:.2f}!''')
elif forma_pagamento == 4:
    num_parcelas = int(input('Quantas parcelas? '))
    if num_parcelas < 3:
        print('INVÁLIDO! APENAS PARCELAS IGUAL A 3 OU ACIMA!')
    else:
        total_juros = preco_compra * 1.20
        print(f'''Sua compra será parcelada em {num_parcelas}x de {total_juros / num_parcelas:.2f} COM JUROS.
    Sua compra de {preco_compra:.2f} vai custar {total_juros:.2f} no final.''')
else:
    print('OPÇÃO INVÁLIDA!')
