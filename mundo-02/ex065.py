"""Exercício Python #065 - Maior e Menor valores"""

total_num = soma_num = maior_valor = menor_valor = 0
validacao_usuario = ' '
while validacao_usuario != 'N':
    num = int(input('Digite um número: '))
    validacao_usuario = input('Quer continuar? [S/N] ').strip().upper()[0]
    total_num += 1
    soma_num += num
    if total_num == 1:
        maior_valor = num
        menor_valor = num
    else:
        if num > maior_valor:
            maior_valor = num
        if num < menor_valor:
            menor_valor = num
media = soma_num / total_num
print(f'''Você digitou {total_num} números e a media deles foi de {media}!
O maior valor digitado foi {maior_valor} e o menor valor foi {menor_valor}!''')
