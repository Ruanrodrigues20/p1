def rotdir(array):
    for i in range(len(array)-1, 0, -1):
        array[i], array[i - 1] = array[i - 1], array[i]


a = [10, 20, 14, 17, 22, 9, 32]
rotdir(a)
assert a == [32, 10, 20, 14, 17, 22, 9]