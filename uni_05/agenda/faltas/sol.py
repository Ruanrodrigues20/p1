def cont_faltas(lista):
    cont = 0
    i = 0
    while i < len(lista):
        if lista[i] == 'f':
            cont += 1
        i += 1
    return cont

cont = 0
while True:
    linha = input()
    if linha == '-': break
    presenca = linha
    if cont_faltas(presenca) > 8:
        cont += 1

print(f'{cont} aluno(s) reprovado(s) por falta.')