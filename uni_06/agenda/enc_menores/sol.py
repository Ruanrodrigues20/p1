def encontra_menores(num, lista):
    for e in lista:
        if e < num:
            return e
    return -1

lista1 = [20, 30, 50, 60]
lista2 = [1, 5, 8, 9]
assert encontra_menores(20, lista1) == -1
assert encontra_menores(30, lista1) == 20
encontra_menores(5, lista2)
assert lista2 == [1, 5, 8, 9]