def submatriz(matriz, p, q, r, s):
    nlins = len(matriz) - 1
    ncols = len(matriz[0]) - 1
    condicao = False

    if  0 <= p <= nlins and 0 <= q <= ncols and 0 <= r <= nlins and 0 <= s <= ncols:
        if p <= r <= nlins and q <= s <= ncols:
            condicao = True
        else:
            condicao = False
    if condicao == False:
        return None

    sub = []
    for l in range(p, r + 1):
        linha = []
        for c in range(q, s + 1):
            linha.append(matriz[l][c])
        sub.append(linha)

    return sub



M = [[11, 12, 13, 14, 15, 16],
         [21, 22, 23, 24, 25, 26],
         [31, 32, 33, 34, 35, 36],
         [41, 42, 43, 44, 45, 46],
         [51, 52, 53, 54, 55, 56],
         [61, 62, 63, 64, 65, 66]]

assert submatriz(M, 1, 3, 3, 4) == [[24, 25],
                                        [34, 35],
                                        [44, 45]]

assert submatriz(M, 2, 3, 5, 7) == None