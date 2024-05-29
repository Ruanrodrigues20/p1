def print_maior(dicionario):
    if len(dicionario) == 0:
        print('', 0)
        return

    maior = 0
    for i in dicionario.keys():
        if dicionario[i] > maior:
            maior = dicionario[i]
            m = i

    print(m, maior)


frase = input()

ocorrencia = {}

for i in range(len(frase)):
    cont = 0
    letra = frase[i]
    for e in frase:
        if e.lower()  == letra.lower():
            cont += 1
    if not letra in ocorrencia:
        ocorrencia[letra.lower()] = cont

print_maior(ocorrencia)