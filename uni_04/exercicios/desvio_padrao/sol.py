def media_seq(seq):
    soma = 0
    for e in seq:
        soma += e
    return (soma / len(seq))


seq1 = [float(elementos) for elementos in input().split()]
seq2 = [float(ele) for ele in input().split()]

media1 = media_seq(seq1)
media2 = media_seq(seq2)

soma1 = 0
for e in seq1:
    soma1 += ((media1 ** 2) - 2 * media1 * e + (e ** 2))

desvio1 = (soma1 / (len(seq1) - 1)) ** (1 / 2)

soma2 = 0
for ele in seq2:
    soma2 += ((media2 ** 2) - 2 * media2 * ele + (ele ** 2))
desvio2 = (soma2 / (len(seq2) - 1)) ** (1 / 2)

if desvio1 > desvio2:
    print(f'A sequência 1 possui o maior desvio padrão ({desvio1:.2f}).')
elif desvio2 > desvio1:
    print(f'A sequência 2 possui o maior desvio padrão ({desvio2:.2f}).')
else:
    print(f'As sequências possuem o mesmo desvio padrão ({desvio1:.2f}).')