num = input()

soma = 0
exp = len(num) - 1
for i in range(len(num)):
    n = int(num[i]) * (2 ** exp)
    soma += n
    print(f'{num[i]} * {2 ** exp} = {n}')
    exp -= 1

print(f'{num}(2) == {soma}(10)')