num = int(input('Enter a number : '))
copy = num
square = num*num
flag = True
while copy:
    if copy % 10 != square % 10 :
       flag = False
       break

    copy = copy // 10
    square= square // 10

    if flag is True :
        print(f'{num} is an automarphic number.')
    else:
        print(f'{num} is not an automorphic number.')    









