class Human:
    email = 'jayabhaskarreddy98@gmail.com'
    address = 'ngo colony, rayachoty'

    def verfiy(self):
        if self.address == 'ngo colony, rayachoty':
            print('Correct')
        else:
            print('Wrong')

    def sent_email(self, msg : str)->None :
        print(msg, type(msg))
        print('email sent')


obj = Human()
print(obj, 'from object')
print(type(obj), 'from object')
obj.sent_email(obj.email)
obj.verfiy()            