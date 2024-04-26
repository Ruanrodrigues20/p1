num1 = int(input())
num2 = int(input())

if num1 == 10 or num2 == 10:
    print('SIM')
elif num1 + num2 == 10:
    print('SIM')
elif num1 != 10 and num2 != 10:
    print('NÃO')
elif num1 + num2 != 10:
    print('NÃO')