while True:
    num = input()
    if num == 'fim': break
    n1 = ''
    n2 = ''
    if len(num) != 8:
        print('Tente novamente.')
    else:
        for i in range(len(num)):
            if i < 4:
                n1 += num[i]
            else:
                n2 += num[i]
        if int(n1, 2) < 10 and int(n2, 2) < 10:
            soma = str(int(n1, 2)) + str(int(n2, 2))
            print(soma)
        else:
            print('BCD inválido.')
