"""Python Exercício #041 - Classificando Atletas"""

from datetime import date
ano_atual = date.today().year

ano_nasci = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasci
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
