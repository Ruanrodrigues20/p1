def noves_fora(lista):
    etapas = []
    valor_fora = lista[0]
    while len(lista) > 1 or lista[0] == 9:
        copia = []
        for i in range(len(lista)):
            copia.append(lista[i])

        etapas.append(copia)

        if len(lista) >=  2:
            valor_fora = (lista[0] + lista[1]) % 9
        else:
            valor_fora = lista[0] % 9

        nova_etapa = [valor_fora]

        for j in range(2, len(lista)):
            nova_etapa.append(lista[j])

        for k in range(len(nova_etapa) - 1):
            if nova_etapa[k] <= nova_etapa[k + 1]:
                nova_etapa[k], nova_etapa[k + 1] = nova_etapa[k + 1], nova_etapa[k]

        lista = nova_etapa

    etapas.append(lista)
    return (valor_fora, etapas)
