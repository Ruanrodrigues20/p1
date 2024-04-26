def dividi3a3(s):
    l = []
    for i in range(0, len(s) - 2, 3):
        string = ''
        string += s[i]
        string += s[i + 1]
        string += s[i + 2]
        l.append(string)
    return l


def inverte3a3(s):
    s1 = dividi3a3(s)
    s2 = ''
    for i in range(len(s1) - 1, -1, -1):
        s2 += s1[i]
    return s2

l1 = 'abcdefghi'
assert inverte3a3(l1) == 'ghidefabc'