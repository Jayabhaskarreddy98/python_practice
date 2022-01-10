class triangle:

    def __init__(self, a, b, c : int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self) -> None:
        perimeter = a + b + c
        print(f'The perimeter of the triangle with {self.a} {self.b} {self.c} is : {perimeter}')

if __name__ == '__main__':
    print('This code is used to find perimeter of triangle')
    a = int(input('Enter the value of a : '))
    b = int(input('Enter the value of b : '))
    c = int(input('Enter the value of c : '))
    obj = triangle(a, b, c)
    obj.perimeter()        
