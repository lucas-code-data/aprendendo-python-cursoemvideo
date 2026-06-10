"""Exercício Python #064 - Tratando vários valores v1.0"""

soma_num = cont_num = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma_num += num
    cont_num += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont_num} números e a soma entre eles foi {soma_num}!')
