def pas_bubble(a):
    trocas = 0
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            trocas += 1
    return trocas


def bublle_sort(a):
    trocas = 0
    while True:
        n_trocas = pas_bubble(a)
        if n_trocas == 0: break

    
a = [14, 3, 12312, 45 , -5]
bublle_sort(a)
print(a)
