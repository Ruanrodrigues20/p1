def anula(lista):
    for i in range(len(lista) -1 , 0, -2):
        if lista[i] + lista[i - 1] == 0:
            lista.pop(i)
            lista.pop(i - 1)


l = [-1, 1, -1, 1, -1]
anula(l)
assert l == [-1]

l2 = [0, 0, 0]
anula(l2)
assert l2 == [0]

l3 = [0, 0, 0, 0]
anula(l3)
assert l3 == []
