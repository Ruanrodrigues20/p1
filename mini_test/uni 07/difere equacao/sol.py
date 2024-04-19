def mesmo_tamanho(lp1, lp2):
    if len(lp1) > len(lp2):
        while True:
            if len(lp1) == len(lp2): break
            lp2.insert(len(lp2), 0)
    elif len(lp2) > len(lp1):
        while True:
            if len(lp2) == len(lp1): break
            lp1.insert(len(lp1), 0)


def subtrai_polinomios(p1, p2):
    resultado = []
    lp1 = [e for e in p1]
    lp2 = [e for e in p2]

    if len(lp1) == 0:
        resultado = [-n for n in lp2]
        return resultado
    elif len(lp2) == 0:
        resultado = [n for n in lp1]
        return resultado

    mesmo_tamanho(lp1, lp2)

    for i in range(len(lp1)):
        sub = lp1[i] - lp2[i]
        resultado.insert(i, sub)

    for j in range(len(resultado) - 1, 0, -1):
        if resultado[j] != 0: break
        if resultado[j] == 0:
            resultado.pop(j)

    return resultado