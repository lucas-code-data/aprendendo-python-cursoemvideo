"""Exercício Python #066 - Vários números com flag"""

total_valores = soma_valores = 0
while True:
    valor = int(input('Digite um valor [999 para parar]: '))
    if valor == 999:
        break
    total_valores += 1
    soma_valores += valor
print(f'A soma dos {total_valores} valores foi {soma_valores}!')
