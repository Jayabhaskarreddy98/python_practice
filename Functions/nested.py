def outer(msg):

    def inner():
        print(msg)
    inner()

outer('Hello !!!')        