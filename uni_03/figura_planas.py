import math

escolha = input().lower()

if escolha == 'triângulo':
    base = float(input())
    altura = float(input())
    area = (base * altura) / 2
    print(f'Área do triângulo: {area:.2f} cm2')
if escolha == 'quadrado':
    lado = float(input())
    area = lado ** 2
    print(f'Area do quadrado: {area:.2f} cm2')
if escolha == 'retângulo':
    lado1 = float(input())
    lado2 = float(input())
    area = lado1 * lado2
    print(f'Area do retângulo: {area:.2f} cm2')
if escolha == 'circulo':
    raio = float(input())
    area = math.pi * (raio ** 2)
    print(f'Area do círculo: {area:.2f} cm2')