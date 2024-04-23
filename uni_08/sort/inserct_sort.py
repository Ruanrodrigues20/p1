def inserct_sort(a):
    n = len(a)
    for i in range(1, n):
        if a[i] < a[i - 1]:
            j = i
            while j > 0:
                if a[j] < a[j -1]:
                    a[j], a[j - 1] = a[j - 1], a[j]
                j -= 1




a = [2, 100, 12, 14, 0, 132, 11, 8, 4, 1]
inserct_sort(a)
print(a)