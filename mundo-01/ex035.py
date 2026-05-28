"""Exercício Python #035 - Analisando Triângulo v1.0"""

print(f'''{'-='*20}
ANALISADOR DE TRIÂNGULOS
{'-='*20}''')

segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento: '))
segmento3 = float(input('Terceiro segmento: '))

if segmento1 + segmento2 > segmento3 and segmento3 + segmento1 > segmento2 and segmento2 + segmento3 > segmento1:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
