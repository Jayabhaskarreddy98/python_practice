class Human:
    email = 'jayabhaskarreddy98@.com'
    address = '560043'

    def verify():
        if Human.address == '560043':
            print('Correct')
        else:
            print('Wrong')

    def sent_email():
        print('email sent')

print(Human.email)
print(Human.address)
Human.sent_email()
Human.verify()                    
