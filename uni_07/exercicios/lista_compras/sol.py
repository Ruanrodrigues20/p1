def adiciona_item(item, lista):
    lista.append(item)
    for i in range(len(lista) -1, 0, -1):
        if lista[i].lower() < lista[i - 1].lower():
            lista[i], lista[i - 1] = lista[i - 1], lista[i]