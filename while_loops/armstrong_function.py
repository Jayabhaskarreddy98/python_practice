def armstrong_number():
    num = int(input('Enter a value : '))
    copy = num
    res = 0
    count = 0
    while copy > 0:
        digit = copy % 10
        count += 1
        res += digit ** count
        copy //= 10
        if num == res:
            print(num, 'is an armstrong number')
    else:
        print(num, 'is not an armstrong number')    