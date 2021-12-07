# program to find factorial of a number

num = int(input('Enter the Number -> '))

fact = 1

if num < 0:
    print('Factorial of negative number is not defined')
else:
    for i in range(1, num + 1):
        fact *= i
    print('Factorial of {} is {}'.format(num, fact))