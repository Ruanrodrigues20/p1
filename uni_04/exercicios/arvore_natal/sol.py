n = int(input())

lista = []
for j in range(1, 2 * n, 2):
    lista.append(j)

for i in range(n):
    linha = (' ' * ((n - i) - 1)) + 'o' * int(lista[i])
    print(linha)

tronco = (' ' * (n - 1)) + 'o'
print(tronco)
