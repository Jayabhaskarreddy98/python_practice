num1 = int(input('Enter a number : '))
num2 = int(input('Enter a number : '))

def perfect():
    res = 0
    for factor in range(1, num+1):
        if num % factor == 0:
            res += factor

def add(num1, num2):
    print(f'{num1} + {num2}')
                
