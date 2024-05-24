def char_unico(string):
    contador = {}
    
    for i in range(len(string)):
        if not string[i] in contador:
            contador[string[i]] = 1
        else:
            contador[string[i]] += 1

    s = ''
    for e in contador.keys():
        if contador[e] == 1:
            s += e  
    return s

s = 'rrrrrruuuuuan'
print(char_unico(s))