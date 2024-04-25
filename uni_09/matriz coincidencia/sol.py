def matriz_coincidência(m1, m2):
    nlins = len(m1)
    ncols = len(m1[0])
    igualdade = [ncols * [0] for i in range(nlins)]
    
    for l in range(nlins):
        for c in range(ncols):
            if m1[l][c] == m2[l][c]:
                igualdade[l][c] = m1[l][c]
    return igualdade

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[10, 11, 12], [13, 14, 15], [7, 8, 9]]
assert matriz_coincidência(m1, m2) == [[0, 0, 0], [0, 0, 0], [7, 8, 9]]

m3 = [[1, 2, 3], [13, 14, 15], [16, 17, 18]]
assert matriz_coincidência(m1, m3) == [[1, 2, 3], [0, 0, 0], [0, 0, 0]]