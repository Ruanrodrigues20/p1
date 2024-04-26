#calculo area dom cilindro

print('Cálculo da Superfície de um Cilindro')
print('---')

med_diametro = float(input('Medida do diâmetro? '))
med_altura = float(input('Medida da altura? '))

pi = 3.14159
raio = med_diametro /2
area = (2 * pi * raio * med_altura) + (2 * pi * (raio **2))

print('---')
print(f'Área calculada: {area:.2f}')
