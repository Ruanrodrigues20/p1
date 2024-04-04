def troca_elementos(lista, origem, destino):
    if origem > destino:
        lista.insert(destino, lista[origem])
        lista.pop(origem + 1)
    elif origem < destino:
        lista.insert(destino, lista[origem])
        lista.pop(origem)

    
l1 = [1, 2, 3, 4, 5]
troca_elementos(l1, 4, 1)
assert l1 == [1, 5, 2, 3, 4]
seq = ['r', 'u', 'a', 'n']
troca_elementos(seq, 2, 1)
assert seq == ['r', 'a', 'u', 'n']
seq2 = ['r', 'u', 'a', 'n']
troca_elementos(seq2, 3, 0)
assert seq2 == ['n', 'r', 'u', 'a']
seq3 = ['a', 'b', 'c', 'd', 'e']
troca_elementos(seq3, -1, 1)
assert seq3 == ['a', 'e', 'b', 'c', 'd']