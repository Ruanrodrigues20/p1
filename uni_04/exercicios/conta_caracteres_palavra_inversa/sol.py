def str_inversa(string):
    inversa = ''
    cont = 0
    for i in range(-1, len(string), -1):
        inversa += string[i]
    for j in range(len(inversa)):
        if string[j] == inversa[j]:
                cont += 1
    return cont


string = input()

cont = str_inversa(string)

print(f'A palavra {string} contém {cont} caractere(s) coincidente(s) com a sua inversa.')