"""Exercício Python #039 - Alistamento Militar"""

from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
idade =  ano_atual - ano_nascimento

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')
if idade < 18:
   print(f'''Ainda faltam {18 - idade} anos para o alistamento.
Seu alistamento será em {ano_atual + (18 - idade)}.''')
elif idade > 18:
   print(f'''Você já deveria ter se alistado há {idade - 18} anos.
Seu alistamento seria em {ano_atual - (idade - 18)}.''')
else:
   print('Você tem que se alistar IMEDIATAMENTE!')
