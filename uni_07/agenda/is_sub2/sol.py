def meu_slice(string, pos):
    s = ''
    count = 0
    if pos > 0:
        for i in range(len(string)):
            if count < pos:
                s += string[i]
            count += 1
    else:
        c = -pos
        for i in range(len(string) - c, len(string)):
            if count > pos:
                s += string[i]
            count -= 1
    return s


def is_substring_expr(str1, str2):
    lista = str2.split('*')
    pre1 = meu_slice(str1, len(lista[0]))
    final = meu_slice(str1, -len(lista[1]))
    return pre1 == lista[0] and final == lista[1]
