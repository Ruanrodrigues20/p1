palavra = input()

senha_final = palavra[0]
vogais = 'aeio'
cod = '4310'
cont = 0

for i in range(1, len(palavra)):
    letra_add = palavra[i]
    for j in range(len(vogais)):
        if palavra[i].lower() == vogais[j]:
            letra_add = cod[j]
            cont += 1

    senha_final += letra_add

print(f'{senha_final} ({cont} troca(s))')
