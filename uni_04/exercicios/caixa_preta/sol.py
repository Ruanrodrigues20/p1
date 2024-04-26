num = int(input())

pode_somar = True
valido = 0
j = 0
for i in range(num):
    dados = [int(x) for x in input().split()]
    peso = dados[0]
    fuel = dados[1]
    altitude = dados[2]

    for j in range(len(dados)):
        if dados[j] >= 0 and pode_somar:
            valido += 1
        else:
            if pode_somar:
                if j == 0:
                    print('dado inconsistente. peso negativo.')
                elif j == 1:
                    print('dado inconsistente. combustível negativo.')
                elif j == 2:
                    print('dado inconsistente. altitude negativa.')

            pode_somar = False

print(f'{valido} dados válidos.')