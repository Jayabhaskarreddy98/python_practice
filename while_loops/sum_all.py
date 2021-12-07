num = int(input('Enter a number : '))
copy = num
res = int()
while copy:
    last_digit = copy % 10
    fact = 1
    for n in range(last_digit, 1, -1):
        fact *= n
        print(fact)
    res += fact
    copy //= 10    

print(res)    
     