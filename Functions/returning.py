def outer(msg):

    def inner():
        print(msg)
    return inner

var = outer('Hello !!!')        

var()