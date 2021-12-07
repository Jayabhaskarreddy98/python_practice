def strong_number():
    num = int(input('Enter a value : '))
    copy = num
    res = 0
    while copy:
        digit = copy % 10
        res += fact (digit)
        copy //= 10
        if res == num:
            print(num, 'It is a strong number')
        else:
            print(num, 'It is not a strong number')
