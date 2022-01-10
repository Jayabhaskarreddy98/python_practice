# prime numbers using functions :-

# function to control everything

def main ():
    num = int(input('Enter the number to check if it is prime or not : '))
    _prime = is_prime(num)
    print_prime_or_not(_prime, num)


def is_prime(num):
    if count_of_factors(num) == 2:
        return True
    return False    

# function to get count of factors

def count_of_factors(num):
    count = 0
    for factor in range(1, num+1):
        if num % factor == 0:
            count = add(count, 1)
    return count              
            
# function to add two int values

def add(num1, num2):
    return num1 + num2

# function to print final result

def print_prime_or_not(flag, num):
    if flag is True:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')
        
main()        

