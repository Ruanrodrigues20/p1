def filas_de_atendimento(fila, n):
    ordem = [[] for _ in range(n)]
    j = 0
    for i in range(len(fila)):
        if j == n:
            j = 0
        ordem[j].append(fila[i])
        j += 1
    return ordem