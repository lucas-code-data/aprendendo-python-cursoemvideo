"""Exercício Python #037 - Conversor de Bases Numéricas"""

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para Hexadecimal''')
opcao_usuario = int(input('Sua opção: '))

if opcao_usuario == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}.')
elif opcao_usuario == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}.')
elif opcao_usuario == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}.')
else:
    print(f'OPÇÃO INVÁLIDA!')
