nome = input()
idade = int(input())

if nome == '' and idade == 0:
    nome = input()
    idade = int(input())

if idade < 5:
    categoria = 'Não pode competir'
else:
    if idade >= 5 and idade <= 7:
        categoria = 'Infantil A'
    elif idade >= 8 and idade <= 10:
        categoria = 'Infantil B'
    elif idade >= 11 and idade <= 13:
        categoria = 'Juvenil A'
    elif idade >= 14 and idade <= 17:
        categoria = 'Juvenil B'
    else:
        categoria = 'Senior'

print(f'{nome}, {idade} anos, {categoria}.')
