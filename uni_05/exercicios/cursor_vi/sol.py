coordenadas = input().split()
x0 = int(coordenadas[0])
y0 = int(coordenadas[1])
continuar = True

while continuar:
    nova_coord = input().split()

    if len(nova_coord) == 0:
        continuar = False
    else:
        coord = int(nova_coord[0])
        direcao = nova_coord[1]

        if direcao == 'h':
            y0 -=  coord
        elif direcao == 'j':
            x0 +=  coord
        elif direcao == 'k':
            x0 -= coord
        elif direcao == 'l':
            y0 += coord

        print(f'[{x0} {y0}]')