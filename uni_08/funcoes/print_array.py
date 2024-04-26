def print_array(array):
    for e in array:
        print(e)
        if e is None: break


a = [10, 20, 3, 4, 5 ,6, None, None, None, None]
print_array(a)