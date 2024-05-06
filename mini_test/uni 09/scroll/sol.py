def scroll(m):
    ncols = len(m[0])
    nlins = (len(m))
    for l in range(nlins):
        for c in range(ncols):
            if l < nlins - 1:
                m[l][c] = m[l + 1][c]
            else:
                m[l][c] = 0
