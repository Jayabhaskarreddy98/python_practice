class square:


   def init(self, side:int) ->None:
       self.side = side

   def area(self):
       area = self.side ** 2
       print(f'The area of the square with {self.side} is : {area}')


if __name__ == '__main__':
    print('This code is used to find the area of a given square')     
    obj = square()
    side = int(input('Enter the side of the square : '))
    obj.init(side)
    obj.area()     




    # after 9th line   def __str__(self):
                          # return f'This square has a side of {self.side}'

               # o = square(16)
               # print(o)          