def imin(array, ini, fim):
    imenor = ini
    for i in range(ini, fim + 1):
        if array[i] < array[imenor]:
            imenor = i
    return imenor


def imax(array, ini, fim):
    imaior = ini
    for i in range(ini, fim + 1):
        if array[i] > array[imaior]:
            imaior = i
    return imaior


def minmax_sort(array):
    processo = []
    ini = 0
    fim = len(array) -1

    for i in range(len(array)):
        if ini >= fim: break

        imenor = imin(array, ini, fim)
        array[imenor], array[ini] = array[ini], array[imenor]

        imaior = imax(array, ini, fim)
        array[imaior], array[fim] = array[fim], array[imaior]

        procedimento = [n for n in array]
        processo.insert(i, procedimento)
        ini += 1
        fim -= 1
    return processo
