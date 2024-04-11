def inserct_sort(a):
    for i in range(len(a) - 1, -1, -1):
        j = i - 1
        while a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
            j -= 1
        print(i, j)
    
            




a = [2, 100, 12, 14, -9, 132, 11, 8, 4, 1]
inserct_sort(a)
print(a)