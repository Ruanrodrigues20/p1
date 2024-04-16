def calcula_digitos_verificacao(cpf):
    string = cpf
    multiplica_01 = 2
    soma1 = 0
    for i in range(len(string) - 1, -1, -1):
        soma1 += int(string[i]) * multiplica_01
        multiplica_01 += 1

    n1 = (10 * soma1) % 11
    if n1 == 10:
        n1 = 0
    string += str(n1)

    soma2 = 0
    multiplica_02 = 2
    for j in range(len(string) - 1, -1, -1):
        soma2 += int(string[j]) * multiplica_02
        multiplica_02 += 1

    n2 = (10 * soma2) % 11
    if n2 == 10:
        n = 0
    string += str(n2)

    return f'{n1}{n2}'