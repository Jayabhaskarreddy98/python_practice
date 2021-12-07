num = int(input('Enter the number : '))
exponent = int(input('Enter exponent value : '))
count = 0
power = 1
copy = num
while copy:
    copy % 10
    count += 1

for i in range(1, exponent + 1):
    power = copy * exponent


print(f'{num} has {count} number of digits') 
print(f'{num} power {exponent} = {power}')