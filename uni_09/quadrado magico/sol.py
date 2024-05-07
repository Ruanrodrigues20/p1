def busca(seq, valor):
    cont = 0
    for i in range(len(seq)):
        if seq[i] == valor:
            cont += 1
    return cont


def repetidos(matriz):
    lista = []
    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
            lista.append(matriz[l][c])

    for i in range(len(lista)):
        if busca(lista, lista[i]) > 1:
            return True
    return False


def eh_quadrado_magico(a):
    ncols = len(a[0])
    nlins = len(a)

    if ncols != nlins:
        return False

    if repetidos(a):
        return False

    valores = []
    d1 = 0
    d2 = 0
    for i in range(nlins):
        d1 += a[i][i]
        d2 += a[i][ncols - i - 1]

    valores.append(d1)
    valores.append(d2)

    for l in range(nlins):
        linha = 0
        for c in range(ncols):
            linha += a[l][c]

        valores.append(linha)

    for c in range(ncols):
        col = 0
        for l in range(nlins):
            col += a[l][c]
        valores.append(col)

    for e in valores:
        if e != d1:
            return False
    return True