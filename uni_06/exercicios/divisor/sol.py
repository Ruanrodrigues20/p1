def divisor(n, lista):
    for i in range(len(lista)):
        if lista[i] % n == 0:
            return i
    return -1