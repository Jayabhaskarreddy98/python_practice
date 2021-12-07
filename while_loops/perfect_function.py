def perfect_number():
    num = int(input('Enter a value : '))
    res = 0
    for i in range(1, num):
        if num%i == 0:
            res = res+1
        if(res == num):
            print(num, 'It is a perfect number')
        else:
            print(num, 'It is not a perfect number')
                    