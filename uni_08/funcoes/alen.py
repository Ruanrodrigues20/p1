def alen(array):
    cont = 0
    for i in range(len(array)):
        if array[i] is None: break
        cont += 1
    return cont


assert alen([3, 4, 6, 7, 9, None, None, None, None]) == 5

