def soma_triade(nums):
    somas = []
    for i in range(len(nums) - 2):
        somas.append(nums[i] + nums[i + 1] + nums[i + 2])
    return somas


def eh_maior(nums):
    maior = nums[0]
    for i in range(len(nums)):
        if nums[i] > maior:
            maior = nums[i]


nums = [int(n) for n in input().split()]
triades = soma_triade(nums)

for i in range(len(triades)):
    if triades[i] == eh_maior(triades):
        break

print('Maior soma:', triades[i])
print('Elemetos:', nums[i], nums[i + 1], nums[i + 2])
print(f'Posicoes {i} {i + 1} {i + 2}')