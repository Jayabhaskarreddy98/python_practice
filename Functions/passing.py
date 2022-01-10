def square(num):
    return num * num

def cube(num):
    return num ** 3

def op(func, num):
    value = func(num)
    print(value)

op(square, 4)
op(cube, 4)            