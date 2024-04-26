ano_atual = int(input('Ano atual? '))
ano_nasc = int(input('Ano de nascimento? '))

idade = ano_atual - ano_nasc

print(f'Idade calculada: {idade} anos')

if idade >= 16:
    print(f'Entrada permitida')
elif idade < 16 and idade >= 14:
    pais = input('Com os pais? ').upper()
    if pais == 'S':
        print('Entrada permitida')
    else:
        print('Entrada proibida para menores de 16 anos sem os pais')
elif idade < 14:
    print('Entrada proibida para menores de 14 anos')
