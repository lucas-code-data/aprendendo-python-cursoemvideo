"""Exercício Python #089 - Boletim com listas compostas"""

from time import sleep

boletim = []
while True:
    nome = str(input('Nome: ')).strip().title()
    try:
        primeira_nota = float(input('Nota 1: '))
        segunda_nota = float(input('Nota 2: '))
    except ValueError:
        print('Erro na leitura das notas!')
        continue
        #validacao para aceitar somente números
    boletim.append([nome, [primeira_nota, segunda_nota]])
    print('-=' * 20)
    while True:
        continuacao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuacao in 'SN':
            break
            #validação com loop que só se encerra após o usuario digitar o que foi solicitado [S/N]
    if continuacao == 'N':
        break
        #se a variavel continuacao estiver em N encerra o programa
print('-=' * 30)
print(f'{"NO.":<5}{"NOME":<10}{"MÉDIA":>5}')
for indice, aluno in enumerate(boletim):
    media_aluno = sum(aluno[1]) / 2
    print(f'{indice:<5}{aluno[0]:<10}{media_aluno:>5}')
print('-' * 25)
while True:
    mostrar_notas = int(input('Mostrar notas de qual aluno? [999 INTERROMPE] '))
    if mostrar_notas == 999:
            print('FINALIZANDO...')
            sleep(1)
            print('<<< VOLTE SEMPRE >>>')
            break
    print(f'Notas de {boletim[mostrar_notas][0]} são: {boletim[mostrar_notas][1]}')
    print('-' * 25)
