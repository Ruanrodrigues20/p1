def remove_menores(n, lista):
    cont = 0
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] < n:
            cont += 1
            lista.pop(i)
    return cont