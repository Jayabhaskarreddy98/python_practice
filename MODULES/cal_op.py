import calculate
def main(flag = True):
    while flag:
        menu()
        choice = int(read('Make your choice : '))
        flag = choose(choice)

def menu():
    print('1.Add\n 2.Sub\n 3.Mul\n 4.Div\n5 5.Exit')

def read(msg):
    return input(msg)

def choose(choice):
    if choice == 5:
        return False
    elif choice == 1:
        print(calculate.add(int(read('Enter 1st number : ')), int(read('Enter 2nd number : '))))
    elif choice == 2:
        print(calculate.sub(int(read('Enter 1st number : ')), int(read('Enter 2nd number : '))))
    elif choice == 3:
        print(calculate.mul(float(read('Enter 1st number : ')), float(read('Enter 2nd number : '))))
    elif choice == 4:
        print(calculate.div(float(read('Enter 1st number : ')), float(read('Enter 2nd number : '))))
    else:
        print('Wrong Input')
    return True 

main()    
    