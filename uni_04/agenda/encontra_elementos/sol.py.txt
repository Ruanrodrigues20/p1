num = int(input())
lista = input().split()

for i in range(len(lista)):
    lista[i] = int(lista[i])

dentro = False
for n in lista:
    if n == num:
        dentro = True

if dentro:
    print('sim')
else: print('não')