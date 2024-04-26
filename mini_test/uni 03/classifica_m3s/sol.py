n = int(input())

if n % 3 == 0:
    if n == 0:
        print('m3, zero')
    else:
        if n > 0:
            sinal = 'positivo'
        elif n < 0:
            sinal = 'negativo'
        if n % 2 == 0:
            imp = 'par'
        else:
            imp = 'ímpar'
        print(f'm3, {sinal} {imp}')
else:
    print('não é mútiplo de 3')
