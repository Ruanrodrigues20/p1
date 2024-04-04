def meu_in(e, seq):
    for ele in seq:
        if ele == e:
            return True
    return False


def verifica_caractere(seq1, seq2):
    string = ''
    if len(seq1) >= len(seq2):
        for e in seq1:
            if not meu_in(e, seq2):
                return e
    else:
        for e in seq2:
            if not meu_in(e, seq1):
                if not meu_in(e, seq1):
                    return e
                

l1 = 'computer'
l2 = 'compter'
assert verifica_caractere(l1, l2) == 'u'
seq1 = 'compter'
seq2 = 'computer'
assert verifica_caractere(seq1, seq2) == 'u'