def validate():
    name = input('Enter your name : ')
    owner = 'pyspiders'

    if name == owner:
        password = input('Enter the password : ')
        if password == 'Jayareddy98':
            print('welcome to pyspiders :-) ')
        else:
            print('password incorrect')
    else:
        print('please get the owner, you are not them.')            