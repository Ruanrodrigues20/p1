def meu_in(e, seq):
    achou = False
    for ele in seq:
        if ele == e:
            achou = True
    return achou


def caractere_ausente(seq1, seq2):
    ausente = ''
    if len(seq1) >= len(seq2):
        for i in range(len(seq1)):
            if meu_in(seq1[i], seq2) == False:
                ausente += seq1[i]
    else:
        for j in range(len(seq2)):
            if meu_in(seq2[j], seq1) == False:
                ausente += seq2[j]
    return ausente

seq1 = 'computer'
seq2 = 'compter'
assert caractere_ausente(seq1, seq2) == 'u'
l1 = 'dolate'
l2 = 'teclado'
assert caractere_ausente(l1, l2) == 'c'
