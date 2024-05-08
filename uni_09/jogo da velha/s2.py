def diagonal(matriz):
    d = [[], []]
    for i in range(len(matriz)):
        d[0].append(matriz[i][i])
        d[1].append(matriz[i][len(matriz) - 1 - i])
    return d


def jogo_da_velha(jogo):
    o_ganhou = False
    x_ganhou = False

    for l in range(len(jogo)):
        if jogo[l] == ['O', 'O', 'O']:
            o_ganhou = True
        elif jogo[l] == ['X', 'X', 'X']:
            x_ganhou = True

    for c in range(len(jogo[0])):
        col = []
        for l in range(len(jogo)):
            col.append(jogo[l][c])

        if col == ['X', 'X', 'X']:
            x_ganhou = True
        elif col == ['O', 'O', 'O']:
            o_ganhou = True
    
    diagonal_1 = diagonal(jogo)[0]
    diagonal_2 = diagonal(jogo)[1]

    if diagonal_1 == ['O', 'O', 'O'] or diagonal_2 == ['O', 'O', 'O']:
        o_ganhou = True
    
    if diagonal_1 == ['X', 'X', 'X'] or diagonal_2 == ['X', 'X', 'X']:
        x_ganhou = True

    if x_ganhou:
        resposta = 'X ganhou'
    elif o_ganhou:
        resposta = 'O ganhou'
    else: 
        resposta = 'Ninguem ganhou'
    
    return resposta


jogo1 = [['O', 'O', 'X'],
         ['X', 'O', 'O'],
         ['O', 'O', 'X']]
assert jogo_da_velha(jogo1) == 'O ganhou'

jogo2 = [['O', 'X', 'X'],
         ['X', 'X', 'O'],
         ['O', 'O', 'X']]
assert jogo_da_velha(jogo2) == 'Ninguem ganhou'