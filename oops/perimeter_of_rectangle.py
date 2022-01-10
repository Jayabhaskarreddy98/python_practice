class rectangle:

    def __init__(self, l, b : int) -> None:
        self.l = l
        self.b = b

    def perimeter(self) -> None:
        perimeter = 2 * (l + b)
        print(f'The area of the rectangle with {self.l} {self.b} is : {perimeter}')

if __name__ == '__main__':
    print('This code is used to find perimeter of rectangle')
    l = int(input('Enter the value of l : '))
    b = int(input('Enter the value of b : '))
    obj = rectangle(l, b)
    obj.perimeter()

