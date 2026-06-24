"""Exercício Python #080 - Lista ordenada sem repetições"""

lista_num = list()
for cont in range(0, 5):
    valores_usuario = int(input('Digite um valor: '))
    if cont == 0 or valores_usuario > lista_num[-1]:
        lista_num.append(valores_usuario)
        print('Valor adicionado ao final da lista!')
    else:
        pos = 0
        while pos < len(lista_num):
            if valores_usuario <= lista_num[pos]:
                lista_num.insert(pos, valores_usuario)
                print(f'Valor adicionado na posição {pos} da lista!')
                break
            pos += 1
print(f'Os valores digitados em ordem são: {lista_num}')
