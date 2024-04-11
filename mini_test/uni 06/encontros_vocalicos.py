def meu_in(ele, seq):
    for e in seq:
        if e == ele:
            return True
    return False


def encontros_vocalicos(string):
    vogais = 'aeiou'
    s_aux = ''
    lista = []
    for car in string:
        if meu_in(car.lower(), vogais):
            s_aux += car
        else:
            if len(s_aux) >= 2:
                lista.append(s_aux)
            s_aux= ''
    if len(s_aux) >= 2:
        lista.append(s_aux)
    return lista

while True:
    stri = input()
    if stri == 'fim': break
    print(encontros_vocalicos(stri))
