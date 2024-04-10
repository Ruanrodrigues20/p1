num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 < (num2 + num3) and num2 < (num1 + num3) and num3 < (num2 +num1):
    condicao = True
else:
    condicao = False

if condicao:
    soma = num1 + num2 + num3
    print(f'triangulo valido. {soma}')
else:
    print(f'triangulo invalido.')