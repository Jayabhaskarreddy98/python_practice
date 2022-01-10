def fabbnoic_series():
 num1 = 0
 num2 = 1
 series = int(input('Enter a value : '))

 while series:

     print(num1)
     _ = num1 + num2
     num1 = num2
     num2 = _
     series -=1
fabbnoic_series()