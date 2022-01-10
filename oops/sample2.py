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
print(id(Human.email))
print(id(obj.email))                    