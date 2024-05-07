def eh_roteiro(iata, voos, rota):
    cidades = [i for i in rota.split('/')]
    for i in range(len(cidades) - 1):
        cid = cidades[i]
        destino = cidades[i + 1]

        if not cid in iata: return False

        ini = iata[cid]
        fim = iata[destino]

        if not fim in voos[ini]:
            return False
    return True