def meu_in(ele, seq):
    for e in seq:
        if ele == e:
            return True
    return False


def verifica_esteira(esteira, cpt):
    lista = []
    for e in esteira:
        if meu_in(e, cpt):
            lista.append(e)

    return lista == cpt


esteira = [2, 1, 3, 4]
componentes = [2, 4]
assert verifica_esteira(esteira, componentes)
assert esteira == [2, 1, 3, 4]
assert componentes == [2, 4]



esteira = [1, 3, 4]
componentes = [4, 1, 3]
assert not verifica_esteira(esteira, componentes)
assert esteira == [1, 3, 4]
