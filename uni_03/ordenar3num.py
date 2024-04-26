def eh_maior(n1, n2, n3):
    if (n1 >= n2) and (n2 >= n3):
        if n2 >= n3:
            maior = n1
            meio = n2
            menor = n3
        elif n2 < n3:
            maior = n1
            meio = n3
            menor = n2
    elif (n2 >= n1) and (n2 >= n3):
        if n1 >= n3:
            maior = n2
            meio = n1
            menor = n3
        else:
            maior = n2
            meio = n3
            menor = n1
    elif (n3 >= n1) and (n3 >= n2):
        if n1 >= n2:
            maior = n3
            meio = n1
            menor = n2
        else:
            maior = n3
            meio = n2
            menor = n1
    return menor, meio, maior


n1 = int(input())
n2 = int(input())
n3 = int(input())

ordem = eh_maior(n1, n2, n3)

print(eh_maior(n1, n2, n3))

print(ordem[0], ordem[1], ordem[2])