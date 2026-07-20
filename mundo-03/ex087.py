"""Exercício Python #087 - Mais sobre Matriz em Python"""

lista = [[], [], []] # 3 sublistas dentro da minha "lista" que é a principal
soma = soma_coluna3 = 0

# um laço dentro do outro para ir adicionando os valores dentro das sublistas 
for linha in range(0, 3):
    for indice in range(0, 3):
        lista[linha].append(int(input(f'Digite um valor para [{linha}, {indice}]: ')))
print('-=' * 30)
for linha in range(0, 3):
    for num in lista[linha]: # acessa cada sublista, começando pela 0 e vai trocando conforme o loop reinicia
        print(f'[ {num:^3} ]', end='')
        if num % 2 == 0: # já calculando os valores pares ao mostrar a matriz
            soma += num
    print() # print vazio para separar as linhas da matriz
print('-=' * 30)
for num in lista: # loop que varre as 3 sublistas
    soma_coluna3 += num[-1] # pega somente o último elemento de cada sublista e soma 
print(f'A soma dos valores pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {soma_coluna3}')
print(f'O maior valor da segunda linha é: {max(lista[1])}') # pega o maior valor somente da segunda sublista
