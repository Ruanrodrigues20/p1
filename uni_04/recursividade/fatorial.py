def fac(n):
    if n == 1:
        return 1

    return n * fac(n - 1)

def fatorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado



n = int(input('Fatorial de: '))

print(fatorial(n))