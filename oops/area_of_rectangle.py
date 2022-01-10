class rectangle:

    def __init__(self, l, b : int) -> None:
        self.l = l
        self.b = b

    def area(self) -> None:
        area = l * b
        print(f'The area of the rectangle with {self.l} {self.b} is : {area}')

if __name__ == '__main__':
    print('This code is used to find area of rectangle')
    l = int(input('Enter the value of l : '))
    b = int(input('Enter the value of b : '))
    obj = rectangle(l, b)
    obj.area()            