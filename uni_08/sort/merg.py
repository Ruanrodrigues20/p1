def merge(array1, array2):
    ordenado = (len(array1) + len(array2)) * [None]
    i1 = 0
    i2 = 0
    j = 0
    while i1 < len(array1) and i2 < len(array2):
        if array1[i1] <= array2[i2]:
            ordenado[j] = array1[i1]
            i1 += 1
        else:
            ordenado[j] = array2[i2]
            i2 += 1
        j += 1
    while i1 < len(array1):
        ordenado[j] = array1[i1]
        i1 += 1
        j += 1
    while i2 < len(array2):
        ordenado[j] = array2[i2]
        i2 += 1
        j += 1

    return ordenado


a = [1, 4, 5, 8, 111]
b = [0, 2, 4, 7, 9]

print(merge(a, b))