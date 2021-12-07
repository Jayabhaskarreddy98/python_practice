# read num
num = int(input('Enter the number : '))
count = 0
# logic to remove each digit one by one
copy = num
while copy:
    copy //= 10
    # count the number of time above logic is run
    count += 1

print(f'{num} has {count} number of digits')     