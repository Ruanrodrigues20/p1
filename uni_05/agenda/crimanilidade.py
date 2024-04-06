def media_lista(nums):
    media = 0
    for e in nums:
        media += e
    return (media / len(nums))


def conv_int(nums):
    lista = []
    for e in nums:
        lista.append(int(e))
    return lista


media_m = float(input())

lista = []
media = 0
while True:
    dado = input()
    if dado == 'fim': break
    valores = conv_int(dado.split())
    if 2 * media_lista(valores) < media_m: break
    if media_lista(valores) > media_m:
        lista.append(dado)

for e in lista:
    print(e)
    