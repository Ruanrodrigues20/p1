def d_matriz(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma


def eh_quadrado_magico(matriz):
    linhas = True
    diagonal = d_matriz(matriz)
    for i in range(len(matriz)):
        soma = 0
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
        if soma != diagonal:
            linhas = False
            break
    
    colunas = True
    for i in range(len(matriz[0])):
        somac = 0
        for j in range(len(matriz)):
            somac += matriz[j][i]
        if somac != diagonal:
            colunas = False
            break
    return linhas and colunas


q = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
assert eh_quadrado_magico(q)

q2 = [[1, 2, 3], [4, 5, 6]]
assert not eh_quadrado_magico(q2)
        