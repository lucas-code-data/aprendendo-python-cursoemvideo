"""Exercício Python #050 - Soma dos pares"""

soma_pares = cont_pares = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° número inteiro: '))
    if num % 2 == 0:
        soma_pares += num
        cont_pares += 1
if cont_pares == 1:
    print(f'Você informou {cont_pares} número par que foi {soma_pares}!')
elif cont_pares > 1:
    print(f'Você informou {cont_pares} números pares e a soma deles é {soma_pares}!')
else:
    print('Você não informou nenhum número par!')