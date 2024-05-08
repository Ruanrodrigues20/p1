def scroll(m):
    ncols = len(m[0])
    nlins = (len(m))
    for l in range(nlins):
        for c in range(ncols):
            if l < nlins - 1:
                m[l][c] = m[l + 1][c]
            else:
                m[l][c] = 0


m = [[  1,  2,  3,  4 ],
     [  5,  6,  7,  8 ],
     [  9, 10, 11, 12 ],
     [ 13, 14, 15, 16 ],
     [ 17, 18, 19, 20 ]]

scroll(m)

assert m == [[  5,  6,  7,  8 ],
             [  9, 10, 11, 12 ],
             [ 13, 14, 15, 16 ],
             [ 17, 18, 19, 20 ],
             [  0,  0,  0,  0 ]]

m1m = [[1, 1, 1]]
scroll(m1m)
print(m1m)