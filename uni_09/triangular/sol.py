def soma_triangular(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    assert nlin == ncol
    
    soma = 0
    c = 0
    for l in range(nlin):
        for c in range(ncol):
            if l <= c:
                soma += matriz[l][c]
    return soma

m = [[1, 1, 1, 1],
     [0, 1, 1, 1],
     [0, 0, 1, 1],
     [0, 0, 0, 1]]

print(soma_triangular(m))