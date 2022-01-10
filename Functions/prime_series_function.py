# prime series using functions :-

# function to control everything

def main():
    print('This is a program to print 1st n prime numbers : ')
    n = int(input('Enter the value of n : '))
    print_n_prime_numbers(n)

# function to get prime series

def print_n_prime_numbers(n):
    count_of_prime_numbers = 0
    num = 2
    while count_of_prime_numbers < n:
        if is_prime(num) is True:
            print(f'{num} is a prime number')
            count_of_prime_numbers = sum((count_of_prime_numbers, 1))
        num = sum((num, 1))

def is_prime(num):
    if count_of_factors(num) == 2:
        return True
    return False

# function to get count of factors

def count_of_factors(num):
    count = 0
    for factor in range(1, num+1):
        if num % factor == 0:
            count = sum((count, 1))
    return count

main()                                 