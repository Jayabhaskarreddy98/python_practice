def main():
    num = int(input('Enter a value : '))
    print_strong_or_not(is_strong(num), num)

def is_strong(num):
    if sum_of_factorials(num) == num:
        return True
    return False

def sum_of_factorials(num):
    import math
    res = 0
    while num:
        last_digit = num % 10
        res = res + math.factorial(last_digit)
        num //= 10
    return res

def print_strong_or_not(flag, num):    
    if flag is True:
        print(f'{num} is a strong number')
    else:
        print(f'{num} is not a strong number')  

main()         