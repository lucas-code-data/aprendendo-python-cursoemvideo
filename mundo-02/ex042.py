"""Exercício Python #042 - Analisando Triângulos v2.0"""

seg1 = int(input('Primeiro segmento: '))
seg2 = int(input('Segundo segmento: '))
seg3 = int(input('Terceiro segmento: '))
if seg1 < seg2 + seg3  and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO ', end='')
    if seg1 == seg2 == seg3:
        print('EQUILATERO')
    elif seg1 != seg2 and seg2 != seg3 and seg3 != seg1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')
