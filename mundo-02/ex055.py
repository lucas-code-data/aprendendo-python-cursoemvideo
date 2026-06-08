"""Exercício Python #055 - Maior e menor da sequência"""

maior_peso = menor_peso = 0
for cont in range(1, 6):
    peso = float(input(f'Peso da {cont}ª pessoa: [KG]'))
    if cont == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
print(f'''O maior peso digitado foi {maior_peso:.2f}KG.
O menor peso digitado foi {menor_peso:.2f}KG.''')
