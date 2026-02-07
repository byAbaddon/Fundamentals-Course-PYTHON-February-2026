while True:
    name = input()
    if name == 'Welcome!':
        print('Welcome to Hogwarts.')
        break
    if name == 'Voldemort':
        print('You must not speak of that name!')
        exit()

    house = ''
    long_name = len(name)
    if long_name < 5:
        house = 'Gryffindor'
    elif long_name == 5:
        house = 'Slytherin'
    elif long_name == 6:
        house = 'Ravenclaw'
    elif long_name > 6:
        house = 'Hufflepuff'

    print(f'{name} goes to {house}.')
