"""Exercício Python #051 - Progressão Aritmética"""

print(f'''{"="*30}
{"10 TERMOS DE UMA P.A":^30}
{"="*30}''')

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
print('='*30)

for c in range(termo, decimo + razao, razao):
    print(c, end = '...')
print('ACABOU!')
