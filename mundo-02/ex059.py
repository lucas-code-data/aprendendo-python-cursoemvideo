"""Exercício Python #059 - Criando um Menu de Opções"""

from time import sleep
valor1= int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opcao_usuario = 0
while opcao_usuario != 5:
    print('-='*20)
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números 
[ 5 ] Sair do programa''')
    print('-='*20)
    opcao_usuario = int(input('Qual é a sua opção? '))
    if opcao_usuario == 1:
        print(f'A soma entre {valor1} e {valor2} é igual a {valor1 + valor2}!')
    elif opcao_usuario == 2:
        print(f'A multiplicação entre {valor1} e {valor2} é igual a {valor1 * valor2}!')
    elif opcao_usuario == 3:
        if valor1 == valor2:
            print('Os dois valores são iguais!')
        else:
            print(f'O maior valor informado é {max(valor1, valor2)}!')
    elif opcao_usuario == 4:
        print('Por favor, informe novos números!')
        sleep(1)
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opcao_usuario == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    sleep(1)
print('Fim do programa! Tenha um bom dia!')
