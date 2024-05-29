def inserct_sort(a):
    n = len(a)
    for i in range(1, n):
        if a[i] < a[i - 1]:
            j = i
            while j > 0:
                if a[j] < a[j -1]:
                    a[j], a[j - 1] = a[j - 1], a[j]
                j -= 1


def anula(lista):
    l = []
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] + lista[j] == 0 and not i in l:
                l.append(i)
    inserct_sort(l)
    for i in range(len(l) -1, -1, -1):
        j = l[i]
        lista.pop(j)
       

                

l = [1, -1, 1, -1]
anula(l)
assert l == []

l2 = [1, 2, -1, 4, -2]
assert l2 == [4]
