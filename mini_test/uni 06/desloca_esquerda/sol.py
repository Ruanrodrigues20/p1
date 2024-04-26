def desloca(lista, origem, destino):
    lista.insert(destino, lista[origem])
    if origem > destino:
        lista.pop(origem + 1)
    elif origem < destino:
        lista.pop(origem)

l1 = [2, 6, 9, 11, 13, 5]
assert desloca(l1, 4, 2) == None
assert l1 == [2, 6, 13, 9, 11, 5]