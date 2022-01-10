class Animal:
    number_of_eyes = '2'
    number_of_brains = '1'
    movement = 'Run'

    def sound():
        if Animal.number_of_eyes == '2':
            print('Correct')
        else:
            print('Wrong')

    def food(bone : str)->None:
        print(bone, type(bone))
        print('eats bone')

Animal.food('eat bone')                    