def agrupa_por_periodo(lista):
    relacao = {}
    for i in range(len(lista)):
        cod = lista[i][:3]
        if not cod in relacao:
            relacao[cod] = 1
        else:
            relacao[cod] += 1
    return relacao

turma = [
        '0511114', '0521137', '0611001',
        '0611003', '0611004', '0621006',
        '0811007', '0811009', '0811502',
        '0811604', '0811605',
        ]

assert agrupa_por_periodo(turma) == {
        '051': 1,
        '052': 1,
        '061': 3,
        '062': 1,
        '081': 5,
    }