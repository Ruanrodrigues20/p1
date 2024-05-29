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

iata = {"Campina Grande": "CPV",
           "Recife": "REC",
           "Salvador": "SSA",
           "Brasilia": "BSB",
           "Sao Paulo": "GRU",
           "Rio de Janeiro": "GIG"}


voos = {"CPV": ["REC", "SSA"],
           "REC": ["CPV", "BSB", "GRU", "GIG"],
           "SSA": ["REC", "GRU", "GIG"],
           "BSB": ["CPV", "GIG", "GRU"],
           "GRU": ["GIG", "BSB"],
           "GIG": ["GRU", "REC"]}

assert eh_roteiro(iata, voos, "Campina Grande/Recife/Rio de Janeiro")
assert eh_roteiro(iata, voos, "Sao Paulo/Rio de Janeiro/Recife/Brasilia")
assert not eh_roteiro(iata, voos, "Recife/Rio de Janeiro/Salvador/Recife")