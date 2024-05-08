def scroll(m):
    for i in range(len(m)):
        nova = []
        if i <= len(m) - 2:
            nova = [n for n in m[i + 1]]
        else:
            nova = len(m[0]) * [0]
        m[i] = nova


m = [[1, 1, 1]]
scroll(m)
print(m)