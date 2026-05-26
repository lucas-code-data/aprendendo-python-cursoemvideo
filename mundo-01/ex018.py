import math
angulo = float(input('Digite o ângulo que você deseja: '))
angulo_rad = math.radians(angulo)
print(f'''O ângulo de {angulo} tem o SENO de {math.sin(angulo_rad):.2f}
O ângulo de {angulo} tem o COSSENO de {math.cos(angulo_rad):.2f}
O ângulo de {angulo} tem o TANGENTE de {math.tan(angulo_rad):.2f}''')
