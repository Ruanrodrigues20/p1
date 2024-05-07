def ordem(lista, elemento):
    lista.append(elemento)
    j = len(lista) - 1

    while lista[j] < lista[j - 1] and j > 0:
        lista[j], lista[j - 1] = lista[j - 1], lista[j]
        j -= 1


def inverte_dicionario(dicionario):
    dic = {}
    for item in dicionario.keys():
        valor = item
        chave = dicionario[item]

        if not chave in dic:
            dic[chave] = []
        if chave in dic:
            ordem(dic[chave], valor)

    return dic