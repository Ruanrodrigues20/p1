x = 0
y = 0
while True:
    movimento = input().split()
    num = int(movimento[1])
    direcao = movimento[0].upper()

    if num == 0:
        print('Fim de jogo')
        break

    if direcao == 'C':
        y += num
    elif direcao == 'B':
        y -= num
    elif direcao == 'E':
        x -= num
    elif direcao == 'D':
        x += num

    if x == 0 and y == 0:
        nao_encontrou = False
    else:
        nao_encontrou = True

    if (2 * x == y or -2 * x == y) and nao_encontrou:
        print(f'Parabéns, conquista do portal ({x}, {y})')
        break