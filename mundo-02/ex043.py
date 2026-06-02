"""Exercício Python #043 - Índice de Massa Corporal"""

peso = float(input('Qual é seu peso? KG '))
altura = float(input('Qual é sua altura? M '))
imc = peso / (altura ** 2)
print(f'Seu IMC é de {imc:.1f}!')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc < 25:
    print('PARABENS! Você está no peso ideal!')
elif imc < 30:
    print('Você está no sobrepeso!')
elif imc <= 40:
    print('CUIDADO! Você está em obesidade!')
else:
    print('CRITICO! VOCÊ ESTÁ EM OBESIDADE MÓRBIDA!!!')
