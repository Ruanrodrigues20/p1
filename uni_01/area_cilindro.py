import math

diametro = float(input('Diametro do ciruclo: '))
altura = float(input('Alura do circulo: '))

pi = math.pi
raio = diametro/2
area_b = pi * raio ** 2
area_l = 2 * pi * raio * altura
area_t = 2 * area_b + area_l

print(f'Area do cilindro é {area_t:.2f}')

