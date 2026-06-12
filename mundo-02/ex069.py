"""Exercício Python #069 - Análise de dados do grupo"""

from time import sleep
mais_18 = homens = mulher_menos20 = 0
while True:
    print(f'''{'-'*30}
{'CADASTRANDO UMA PESSOA':^30}
{'-'*30}''')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-'*30)
    if idade >= 18:
        mais_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menos20 += 1
    continuacao = ' '
    while continuacao not in 'SN':
        continuacao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuacao == 'N':
        print('Encerrando...')
        sleep(1)
        print('Programa de cadastos encerrado com sucesso!')
        print('-'*30)
        break
print(f'''Total de pessoas com mais de 18 anos: {mais_18}
Ao todo temos {homens} homem/homens cadastrado.
E temos {mulher_menos20} mulher/mulheres com menos de 20 anos.''')

    
