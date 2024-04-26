def caixa_registradora(lista, meta):
    vendas =  0.0
    comicao = 0.0
    for e in lista:
        vendas += e
        if e < 1000:
            comicao += (e * 5) / 100
        elif 1000 <= e < 5000:
            comicao += (e * 10) / 100
        else:
            comicao += (e * 15) / 100
    if (vendas - comicao) >= meta:
        situacao = 'Lucro'
    else:
        situcao = 'Prejuizo'
    return [vendas, comicao, situacao]
