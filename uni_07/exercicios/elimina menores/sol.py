def elimina_menores(num,lista):
    cont_menor = 0
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] < num:
            lista.pop(i)
            cont_menor += 1
    return cont_menor


l1 = [100, 200, 300, 400]
assert elimina_menores(100, l1) == 0
assert l1 == [100, 200, 300, 400]

lista2 = [3,5,1,7,10,9]
assert elimina_menores(4, lista2) == 2
assert lista2 == [5,7,10,9]

l3 = []
assert elimina_menores(5, l3) == 0
assert l3 == []
