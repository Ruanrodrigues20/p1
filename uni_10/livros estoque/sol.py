def ausentes(estoque):
    cont = 0
    for item in estoque.keys():
        if estoque[item] == 0:
            cont += 1
    return cont