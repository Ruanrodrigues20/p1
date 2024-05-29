def num_creditos(bd_ufcg, matricula):
    soma = 0
    for i in bd_ufcg.keys():
        unidade = bd_ufcg[i]
        for cadeira in unidade.keys():
            if matricula in unidade[cadeira]:
                soma += cadeira[1]

    return soma
