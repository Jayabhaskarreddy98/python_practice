class circle:

    def __init__(self, r : int) -> None:
        self.r = r

    def area(self) -> None:
        area = 3.14 * (r ** 2)
        circumference = 2 * 3.14 * self.r
        print(f'The area of the circle with {self.r} is : {area}')
        print(f'The circumference of the circle with {self.r} is : {area, circumference}')

if __name__ == '__main__':
    print('This code is used to find area of circle')
    print('This code is used to find circumference of circle')
    r = int(input('Enter the value of r : '))
    obj = circle(r)
    obj.area()            