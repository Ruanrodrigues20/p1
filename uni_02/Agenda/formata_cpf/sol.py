n1 = int(input())
n2 = int(input())
n3 = int(input())

pri_n1 = n1 // (100)
ultimos2_n1 = n1 % 100
ult_n1 = n1 % 10
ult1_n1 = n1 % 100 // 10
soma_1 = ult_n1 + ult1_n1

pri_n2 = n2 // (100)
ultimos2_n2 = n2 % 100
ult_n2 = n2 % 10
ult1_n2 = n2 % 100 // 10
soma_2 = ult_n2 + ult1_n2

pri_n3 = n3 // (100)
ultimos2_n3 = n3 % 100
ult_n3 = n3 % 10
ult1_n3 = n3 % 100 // 10
soma_3 = ult_n3 + ult1_n3


print(f'{pri_n1}-{ultimos2_n1}')
print(soma_1)
print(f'{pri_n2}-{ultimos2_n2}')
print(soma_2)
print(f'{pri_n3}-{ultimos2_n3}')
print(soma_3)