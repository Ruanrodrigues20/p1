def matriz_coincidencia(m1, m2):
    ncols = len(m1[0])
    nlins = len(m1)
    m = [ncols * [0] for i in range(nlins)]

    for l in range(nlins):
        for c in range(ncols):
            if m1[l][c] == m2[l][c]:
                m[l][c] = m1[l][c]

    return m

M1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

M2= [[10, 11, 12],
     [13, 14, 15],
     [ 7,  8,  9]]

M3= [[ 1,  2,  3],
     [13, 14, 15],
     [16, 17, 18]]

assert matriz_coincidencia(M1, M2) == [[0,0,0],[0,0,0],[7,8,9]]

assert matriz_coincidencia(M1, M3) == [[1,2,3],[0,0,0],[0,0,0]]