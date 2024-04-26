def eh_duplicada(string):
    seq = string.split()
    igual = False
    metade1 = ''
    for i in range(len(seq) // 2):
        metade1 += seq[i]
    metade2 = ''
    for j in range(len(seq) // 2 - len(seq)):
        metade2 += seq[j]
    if metade1 == metade2:
        return metade1
    return seq


n = input()
nums = n

if eh_duplicada(nums) != len(n):
    condicao = len(nums) // 2
    for i in range(len(eh_duplicada(nums))):
        if i < len(nums) - 1:
            print(nums[i], end = '')
        else:
            print(nums[i])
else:
    print(n)