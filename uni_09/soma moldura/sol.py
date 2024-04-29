def soma_moldura(matriz, k):
    soma_l1 = 0
    soma_l2 = 0
    for i in range(k, len(matriz[k]) - k):
        soma_l1 += matriz[k][i]
        soma_l2 += matriz[-k - 1][i]
    print(soma_l1, soma_l2)
    
    soma_c1 = 0
    soma_c2 = 0
    for l in range(1, len(matriz) - k):
        print(matriz[l][k])
        soma_c1 += matriz[l][k]
        soma_c2 += matriz[l][-k - 1]
    print(soma_c1, soma_c2)

                                            

m = [[1, 1, 999, 1], 
     [2, 3, 4, 1],
     [1, 2, 3, 1],
     [1, 1, 1, 1]]
soma_moldura(m, 2)