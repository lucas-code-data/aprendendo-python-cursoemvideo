"""Exercício Python #054 - Grupo da Maioridade"""

from datetime import date
ano_atual = date.today().year
menor_idade = maior_idade = 0
for cont in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {cont}ª pessoa nasceu? '))
    if (ano_atual - ano_nascimento) < 18:
        menor_idade += 1
    else:
        maior_idade += 1
print(f'''Ao todo tivemos {maior_idade} pessoas maiores de idade.
E também tivemos {menor_idade} pessoas menores de idade.''')
