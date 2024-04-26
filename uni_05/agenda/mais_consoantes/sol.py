def cont_consoante(p):
    cont = 0
    for e in p.lower():
        if ord(e) > 97 and ord(e) <= 122 and ord(e) != 101 and ord(e) != 105 and ord(e) != 111 and ord(e) != 117:
            cont += 1
    return cont

def cont_vogais(p):
    cont = 0
    for e in p.lower():
        if ord(e) == 97 or ord(e) == 101 or ord(e) == 105 or ord(e) == 111 or ord(e) == 117:
            cont += 1
    return cont

cont = 1
while True:
    palavra = input()
    if cont_consoante(palavra) <=  cont_vogais(palavra):
        cont += 1
    else: break

print(cont)
