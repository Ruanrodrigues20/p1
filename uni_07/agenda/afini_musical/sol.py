def meu_in(elem, seq):
    for e in seq:
        if e == elem:
            return True
    return False


def tem_afinidade(l1, l2):
    cont = 0
    if l1 > l2:
        for i in range(len(l1)):
            if meu_in(l1[i], l2):
                cont += 1
    else:
        for i in range(len(l2)):
            if meu_in(l2[i], l1):
                cont += 1
    return cont >= 3


l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
l2 = ['zeze', 'joao', 'u2', 'jquest']
assert tem_afinidade(l1, l2) == True

seq1 = ['nadson', 'japaozin', 'nattan']
seq2 = ['nadson', 'japaozin', 'nattan', 'mari fernades']
assert tem_afinidade(seq1, seq2) == True