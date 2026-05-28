"""Exercício Python #029 - Radar eletrônico"""

velocidade_atual = float(input('Qual é a velocidade atual do carro? KM'))
if velocidade_atual > 80:
    multa = (velocidade_atual - 80) * 7
    print(f'''MULTADO! Você excedeu o limite que é de 80KM/H.
    Você deve pagar uma multa no valor de R${multa:.2f}!''')
print('Tenha um bom dia! Dirija com cuidado!')
