def difere(lista):
    l = [n for n in lista]
    for i in range(len(l) -1 , 0, -1):
        if l[i] == l[i - 1]:
            l.pop(i)
    return l

while True:
    n = [int(num) for num in input().split()]
    if n == [999]: break
    print(difere(n))
    