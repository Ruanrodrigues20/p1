def hexa(num):
    if ord(num) >= 48 and ord(num) <= 57:
        return int(num)
    cars = 'abcdef'
    numeros = [10, 11, 12, 13, 14, 15]
    for i in range(len(cars)):
        if cars[i] == num:
            return numeros[i]

n = input()

exp = len(n) - 1
soma = 0
for i in range(len(n)):
    num = hexa(n[i])
    num_d = num * 16 ** exp
    soma += num_d
    print(f'{num} * 16^{exp} = {num_d}')
    exp -= 1

print(f'---')
print(f'{n}(16) = {soma}(10)')