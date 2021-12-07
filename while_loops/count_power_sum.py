num = int(input('Enter a number'))

copy = num
count = 0
res = 0
while copy:
    copy //= 10
    count += 1

copy = num
while copy:
    digit = copy % 10
    copy //= 10
copy = num
while copy:
    digit = copy % 10
    copy //= 10
    res = res + digit ** count
    print(f'{digit} sum are {res}') 

if res == num:
    print('amostrong number')
else:
    print('not an amostrong number')             
