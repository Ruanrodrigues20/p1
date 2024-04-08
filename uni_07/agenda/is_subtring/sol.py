def divide_str(s, num):
    lista = []
    j = 0
    for i in range(0, len(s)):
        count = 0
        s1 = ''
        j = i
        while count < num and j < len(s):
            s1 += s[j]
            count += 1
            j += 1
        if len(s1) == num:
            lista.append(s1)
    return lista


def meu_in(ele, seq):
    for e in seq:
        if ele == e:
            return True
    return False


def is_substring(str1, str2):
    lista = divide_str(str1, len(str2))
    if meu_in(str2, lista):
            return True
    return False


assert is_substring('boiada', 'oi')
assert not is_substring('casorio', 'casa')