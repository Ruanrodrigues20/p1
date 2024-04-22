def separa_duas_cores(array, cor1, cor2):
    l = 0
    for i in range(len(array)):
        if array[i] == cor1:
            array[i], array[l] = array[l], array[i]
            l += 1


a = ['a', 'b', 'b', 'a', 'b']
separa_duas_cores(a, 'b', 'a')
assert a == ['b', 'b', 'b', 'a', 'a']

array = [0, 1, 0]
separa_duas_cores(array, 0, 1)
assert array == [0, 0, 1]

array = [0, 1, 0]
separa_duas_cores(array, 1, 0)
assert array == [1, 0, 0]