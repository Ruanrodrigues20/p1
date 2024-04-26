def troca(lista):
    for i in range(0, len(lista) - 2, 2):
        print(i)
        if lista[i] < lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
    
while True:
    l = input().split()
    troca(l)
    print(l)