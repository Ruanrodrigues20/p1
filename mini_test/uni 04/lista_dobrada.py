def lista_dobrada(lista):
    metade1 = ''
    for i in range(len(lista) // 2):
        metade1 += lista[i]
    metade2 = ''
    for j in range(len(lista) // 2, len(lista)):
        metade2 += lista[j]
    return metade1 == metade2


nums = input().split()

if lista_dobrada(nums) and len(nums) % 2 == 0:
    for i in range(len(nums) // 2):
        if i < len(nums) // 2:
            print(nums[i], end = ' ')
        else:
            print(nums[i])
else:
    for i in range(len(nums)):
        if i < len(nums):
            print(nums[i], end = ' ')
        else:
            print(nums[i])