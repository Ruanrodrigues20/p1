def rotaciona90(imagem):
    t = []
    for c in range(len(imagem[0])):
        linha = []
        for l in range(len(imagem)-1, -1, -1):
            linha.append(imagem[l][c])
        t.append(linha)
    return t