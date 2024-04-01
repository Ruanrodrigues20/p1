x = int(input())
y = int(input())

soma = 0
inter = [n for n in range(x, y + 1)]
for e in inter:
    if e % 13 != 0:
        soma += e
print(soma)