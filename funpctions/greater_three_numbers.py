def greater():
    num1 = int(input('Enter the first number : '))
    num2 = int(input('Enter the second number : '))
    num3 = int(input('Enter the third number : '))
    if(num1 > num2) and (num1 > num3):
        print('num1 is greater')
    elif(num2 > num3):
        print('num2 is greater')
    else:
        print('num3 is greater')

# print(greater)
greater() # function call