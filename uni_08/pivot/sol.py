def pivot(nums):
    p = nums[0]
    prox = 0
    for i in range(len(nums)):
        num = nums[i]
        if num <= p:
            j = i
            while j > prox:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            if num != p:
                prox += 1

seq = [6,4,8,1,7,3]
pivot(seq)
assert seq == [4, 1, 3, 6, 8, 7]