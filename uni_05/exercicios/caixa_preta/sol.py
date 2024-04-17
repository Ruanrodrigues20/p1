flag = True
cont_p = 0
cont_c = 0
cont_a = 0
while True:
    dados = input().split()
    peso = int(dados[0])
    fuel = int(dados[1])
    alt = int(dados[2])

    if peso >= 0: cont_p += 1
    if peso >= 0 and fuel >= 0: cont_c += 1
    if peso >= 0 and fuel >= 0 and alt >= 0: cont_a += 1

    if peso < 0 or fuel < 0 or alt < 0 and flag:
        if peso < 0:
            print(f'dado inconsistente. peso negativo.')
        elif fuel < 0:
            print(f'dado inconsitente. combustível negativo.')
        elif alt < 0:
            print(f'dado inconsistente. altitude negativa.')
        break

print(f'peso: {cont_p}')
print(f'combustível: {cont_c}')
print(f'altitude: {cont_a}')