def blefe(array):
    a = len(array) * [None]
    for i in range(len(array) - 1):
        if array[i + 1] > array[i]:
            a[i + 1] = array[i + 1] - array[i]
            array[i + 1] = array[i]
    for j in range(len(a)):
        if a[j] is None:
            a[j] = 0
    return a


a1 = [9, 4, 5, 3, 1]
blefe(a1)
assert a1 == [9, 4, 4, 3, 1]