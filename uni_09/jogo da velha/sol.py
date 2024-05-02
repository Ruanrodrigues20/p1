def jogo_da_velha(jogo):
    nlins = 3
    ncols = 3
    lista = []
    for l in range(nlins):
        lista.append(jogo[l])

    d1 = []
    d2 = []
    for i in range(nlins):
        d1.append(jogo[i][i])
        d2.append(jogo[i][ncols - i - 1])

    lista.append(d1)
    lista.append(d2)

    for c in range(ncols):
        colunas = []
        for l in range(nlins):
            colunas.append(jogo[l][c])
        lista.append(colunas)

    x = False
    o = False

    for e in lista:
        if e == ['X', 'X', 'X']:
            x = True
        if e == ['O', 'O', 'O']:
            o = True

    if x and o:
        vitoria = 'Ninguem ganhou'
    elif x:
        vitoria = 'X ganhou'
    elif o:
        vitoria = 'O ganhou'
    else:
        vitoria = 'Ninguem ganhou'

    return vitoria

j1 = [['O', 'O', 'X'], ['X', 'O', 'O'], ['O', 'O', 'X']]
print(jogo_da_velha(j1))