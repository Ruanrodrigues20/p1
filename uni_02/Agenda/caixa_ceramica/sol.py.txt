revestimento = float(input('Capacidade de revestimento? '))
print('')

print('== Dados do vão a revestir ==')

compr = float(input('Comprimento? '))
larg = float(input('Largura? '))
alt = float(input('Altura? '))
print('')

area = (compr * larg) + (2 * alt * compr) + (2 * larg * alt)
t_caixas = int(area / revestimento)

print('== Resultados ==')
print(f'Área total a revestir: {area:.1f} m2')
print(f'Número de caixas: {t_caixas}')