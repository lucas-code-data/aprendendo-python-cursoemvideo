"""Exercício Python #056 - Analisador completo"""

media_idade = homem_maisvelho = mulheres_menos20 = 0
nome_Hmaisvelho = ''
for cont in range(1, 5):
    print(f'----- {cont}ª PESSOA -----')
    nome = input('Nome: ').strip().upper()
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F]').strip().upper()[0]
    media_idade += idade
    if cont == 1 and sexo == 'M':
        homem_maisvelho = idade
        nome_Hmaisvelho = nome  
    else:
        if sexo == 'M' and idade > homem_maisvelho:
            homem_maisvelho = idade
            nome_Hmaisvelho = nome
    if idade < 20 and sexo == 'F':
        mulheres_menos20 += 1
print(f'A media de idade do grupo é de {media_idade / 4} anos.')
if homem_maisvelho >= 1:
    print(f'O homem mais velho do grupo tem {homem_maisvelho} anos e se chama {nome_Hmaisvelho}.')
else:
    print('Não há nenhum homem no grupo!')
print(f'Ao todo são {mulheres_menos20} mulher/mulheres com menos de 20 anos.')
