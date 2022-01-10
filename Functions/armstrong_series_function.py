# main to control everything
def main():
    print('This code checks if given number is a armstrong number or not? ')
    n = input('Enter a number : ')
    print_armstrong_or_not(int(n)) if n.isnumeric() else print_armstrong_or_not()

# function to perform the armstrong operation
def armstrong(num):
    power = count_of_digits(num)
    res = 0 
    while num:
        last_digit = num % 10
        res = sum((res, pow(last_digit, power)))
        num = remove_last_digit(num)
    return res

# function to count the number of digits of a given number
def count_of_digits(num):
    count = 0    
    while num:
        num = remove_last_digit(num)
        count = sum((count, 1))
    return count

def remove_last_digit(num):
    return num // 10

def print_armstrong_or_not(n=12):
    num = 1
    count = 0
    while count < n:
        if armstrong(num) == num:
            print(f'{num} is an armstrong number')   
            count = sum((count, 1))
        num = sum((num, 1))   

main()        



