def alen(a):
    cont = 0
    for e in a:
        if e is None: break
        cont += 1
    return cont


def mov_lado(ele, array, direcao):
    for i in range(alen(array) - 1):
        if array[i] != array[i - 1] and direcao == 0:
            array[i], array[i - 1] = array[i - 1], array[i]
        elif array[i] != array[i + 1] and direcao == 1:
            array[i], array[i + 1] = array[i + 1], array[i]

def separa_duas_cores(array, cor1, cor2):
    for i in range(alen(array) - 1):
        if array[i] != cor2:
            mov_lado(array[i], array, 1)
        else:
            mov_lado(array[i], array, 0)



a = ['a', 'b', 'b', 'a', 'b']
separa_duas_cores(a, 'b', 'a')
print(a)

array = [0, 1, 0]
separa_duas_cores(array, 0, 1)
assert array == [0, 0, 1]

array = [0, 1, 0]
separa_duas_cores(array, 1, 0)
assert array == [1, 0, 0]