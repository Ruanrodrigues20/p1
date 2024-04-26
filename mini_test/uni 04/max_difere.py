def max_diferenca(lista):
    difere = []
    for i in range(len(lista) - 1):
        difere.append(abs(lista[i] - lista[i + 1]))
    return difere


def eh_maior(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior


nums = [float(n) for n in input().split()]

diferencas = max_diferenca(nums)
for i in range(len(diferencas) - 1):
    if diferencas[i] == eh_maior(diferencas):
        n1 = nums[i]
        n2 = nums[i + 1]

print(n1, 'e', n2)
    