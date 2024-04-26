def maior(array, pos):
    i_m = 0
    maior = array[0]
    for i in range(0, pos + 1):
        if array[i] > maior:
            maior = array[i]
            i_m = i
    return i_m

def select_sort(array):
    for i in range(len(array) -1, -1, -1):
        i_n = maior(array, i)
        if array[i_n] > array[i]:
            array[i], array[i_n] = array[i_n], array[i]
            


a = [2, 100, 12, 14, -9, 132, 11, 8, 4, 1]
select_sort(a)
print(a)