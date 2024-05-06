def transporta(matriz):
    mt = []
    for c in range(len(matriz[0])):
        linha = []
        for l in range(len(matriz)):
            linha.append(matriz[l][c])
        mt.append(linha)
    return mt

m = [[1, 2], [3, 4]]

assert transporta(m) == [[1, 3], [2, 4]]
        