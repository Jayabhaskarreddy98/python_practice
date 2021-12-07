num = int(input('Enter a number : '))

copy = num
count = 0
while copy:
    copy //= 10
    count += 1

copy = num
while copy:
    digit = copy % 10
    print(f'{digit} power {count} = {digit ** count}')
    copy //= 10    