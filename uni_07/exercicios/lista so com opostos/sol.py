def lista_so_com_oposto(lista):
    for i in range(len(lista) - 1, -1, -1):
        remove = True
        for j in range(len(lista) - 1, -1, -1):
            if int(lista[i]) + int(lista[j]) == 0:
                remove = False
        if remove:
            lista.pop(i)
