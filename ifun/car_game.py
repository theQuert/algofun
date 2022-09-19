import math, random

command = input('>')
started = False
while command.lower() != 'quit':
    if command == 'help':
        print('''start - to start the car
stop - to stop the car
quit - exit
        ''')
    elif command == 'start':
        if not started:
            print('Car started... Ready to go !')
            started = True
        else:
            print('Car is already started...')
            started = True
    elif command == 'stop':
        if started:
            print("Car has already stopped")
            started = False
        else:
            print('Car is stopped before breaking.')
            started = False
    elif command == 'quit':
        break
    else:
        print("I don't understand...")
    command = input('>')

