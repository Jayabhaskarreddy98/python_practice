num = int(input('Enter a number'))
res = 0
for i in range(1, num):
    if(num%i==0):
        res=res+i
if(res==num):
    print('perfect number')
else:
    print('not a perfect number')            