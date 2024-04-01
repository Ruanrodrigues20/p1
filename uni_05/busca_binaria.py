import math

lista  = [i for i in input().split()]
lista.sort()
n = int(input())
i = 0
j = len(lista) - 1
while j >= i:
    k = math.floor((i + j) / 2)
    if lista[k] != n:
        if n < lista[k]:
            j -= 1
        elif n > lista[i]:
            i += 1
    else:
        print(f'Achei {lista[k]} posicao{k}')
        break