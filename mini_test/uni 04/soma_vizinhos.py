def soma_vizinho(lista):
    soma = []
    for i in range(1, len(lista) - 1):
        soma.append(int(lista[i - 1]) + int(lista[i + 1]))
    return soma

n = int(input())

nums = []
for k in range(n):
    nums.append(int(input()))

somas = soma_vizinho(nums)
somat = 0
if len(nums) % 2 == 0:
    for i in range(len(somas)):
        if somas[i] == nums[i + 1]:
            somat += nums[i + 1]
else:
    for j in range(len(nums)):
        if j < len(somas) and somas[j] == nums[j + 1]:
            somat += nums[j + 1]

print(somat)