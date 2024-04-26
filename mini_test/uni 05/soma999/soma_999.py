soma = 0
lista = []
cont = 0
while True:
    num = int(input())
    lista.append(num)
    cont += 1
    soma += num
    if soma >= 999: break

media = soma / cont 

i = 0
cont_m = 0
while i < cont:
    if lista[i] > media:
        cont_m += 1
    i += 1

print(soma)
print(media)
print(cont_m)