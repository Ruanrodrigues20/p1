def eh_bissexto(n):
    return (n % 400 == 0 or (n % 4 == 0 and n % 100 != 0))

ano1 = int(input())
ano2 = int(input())
ano3 = int(input())
b1 = 0
b2 = 0
b3 = 0
bissexto = 0

if eh_bissexto(ano1):
    b1 = ano1
if eh_bissexto(ano2):
    b2 = ano2
if eh_bissexto(ano3):
    b3 = ano3

if b1 != 0 or b2 != 0 or b3 != 0:
    if b1 >= b2 and b1 >= b3:
        bissexto = b1
    elif b2 >= b1 and b2 >= b3:
        bissexto = b2
    elif b3 >= b1 and b3 >= b2:
        bissexto = b3
    print(f'{bissexto}')
else:
    print('Nenhum ano é bissexto!')