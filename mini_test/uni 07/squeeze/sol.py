def squeeze(valores):
    lista = [e for e in valores]
    for i in range(len(lista) - 1, 0, -1):
        if lista[i] == lista[i - 1]:
            lista.pop(i)
    return lista


nums = [3, 1, 1, 1, 4, 7, 3, 3, 2, 7]
assert squeeze(nums) == [3, 1, 4, 7, 3, 2, 7]
assert nums == [3, 1, 1, 1, 4, 7, 3, 3, 2, 7]

v = [7, 3, 3, 5, 8, 8, 8, 8, 4, 3]
assert squeeze(v) == [7, 3, 5, 8, 4, 3]
