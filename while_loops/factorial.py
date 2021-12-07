# read num
num = int(input('Enter a number : '))
# logic to get each digit from the num
copy = num
while copy:
    digit = copy % 10
    # logic for factorial of each digit
    fact = 1
    for n in range(digit,1,-1):
        fact *= n
    print(f'{digit}! = {fact}')
    copy //= 10      