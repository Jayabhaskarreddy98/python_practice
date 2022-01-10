class Human:
    email = 'jayabhaskarreddy98@gmail.com'
    address = 'ngo colony, rayachoty'

    def verfiy():
        if Human.address == 'ngo colony, rayachoty':
            print('Correct')
        else:
            print('Wrong')

    def sent_email(msg : str)->None :
        print(msg, type(msg))
        print('email sent')

obj = Human()
print(Human.email)
print(obj.email)
print(id(Human.email), 'using class')
print(id(obj.email), 'using obj')
obj.email = 'jayabhaskarreddy007gmail.com'
print(Human.email)
print(obj.email)
print(id(Human.email), 'using class')
print(id(obj.email), 'using obj')