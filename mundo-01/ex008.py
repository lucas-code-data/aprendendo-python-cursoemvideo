distancia = float(input('Distância em metros: '))
print(f'''A medida de {distancia:.1f} corresponde a
{distancia / 1000}km
{distancia / 100}hm
{distancia / 10}dam
{distancia * 10:.0f}dm
{distancia * 100:.0f}cm
{distancia * 1000:.0f}mm''')