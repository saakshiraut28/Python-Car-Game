command = ""
is_start = False
is_stop = False
while True:
    command = input('>').lower()
    if command == 'start':
        if is_start:
            print('The car is already started.')
        else:
            is_start = True
            print('the car is started')
    elif command == 'stop':
        if is_stop:
            print('It has already been stop')
        else:
            is_stop = True
            print('the car is stopped')
    elif command == 'help':
        print('''Start:to start the car.
Stop: to stop the car.
Quit: to end the game.''')
    elif command == 'quit':
        break
    else:
        print('Invalid Input')