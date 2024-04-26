def alen(array):
    cont = 0
    for i in range(len(array)):
        if array[i] is None: break
        cont += 1
    return cont


def a_insert(array, ele, pos):
    assert 0 <= pos <= alen(array)
    for i in range(alen(array) - 1, pos - 1, -1):
        array[i + 1] = array[i]
    array[i] = ele


a = [1, 2, 3, 4, 5, 6, None, None]

a_insert(a, 10, 4)
print(a)
