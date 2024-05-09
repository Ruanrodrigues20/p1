def anula(lista):
    if len(lista) % 2 == 0:
        for i in range(len(lista) -2, 0, -1):
            if lista[i] + lista[i - 1] == 0:
                lista.pop(i)
                lista.pop(i - 1)
    else:
        for i in range(len(lista) -1, 1, -1):
            if lista[i] + lista[i - 1] == 0:
                lista.pop(i)
                lista.pop(i - 1)
    
l = [0, 0]
anula(l)
print(l)