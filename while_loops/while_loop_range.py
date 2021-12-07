num1 = int(input('Enter the starting point for the range -> '))
num2 = int(input('Enter the ending point for the range -> '))
_ = num1
res = int()
while _ <= num2:
    res += _
    _ += 1

print(f' sum of all the numbers in range from {num1} to {num2} is {res} ')
    