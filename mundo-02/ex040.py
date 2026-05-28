"""Exercício Python #040 - Aquele clássico da Média"""

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Tirando {nota1} e {nota2}, a média do aluno é {media:.1f}!')
if media >= 7:
    print('O aluno ESTÁ APROVADO! PARABENS!')
elif media >= 5:
    print('O aluno ESTÁ DE RECUPERAÇÃO! BOA SORTE NOS ESTUDOS!')
else:
    print('O aluno ESTÁ REPROVADO! SE ESFORCE MAIS!')
