def agrupa_multiplos(array, k):
    prox_pos = 0
    for i in range(len(array)):
        if array[i] % k == 0:
            i_divisor = i
            while i_divisor > prox_pos:
                array[i_divisor], array[i_divisor - 1] = array[i_divisor - 1], array[i_divisor]
                i_divisor -= 1
            prox_pos += 1


seq = [6, 15, 12, 6, 8, 3, 25, 14, 1, 10, 7]

agrupa_multiplos(seq, 5)
assert seq == [15, 25, 10, 6, 12, 6, 8, 3, 14, 1, 7]

agrupa_multiplos(seq, 2)
assert seq == [10, 6, 12, 6, 8, 14, 15, 25, 3, 1, 7]
