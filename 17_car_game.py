previous_command = ''
started = False

while True:
    command = input("> ").lower()
    if command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit """)  # multiline output, best for emails and best formatting, printed as is
    elif command == 'start':
        if started:
            print("Car already started...")
            continue
        else:
            started = True
            print("Car started.... ready to go")
    elif command == 'stop':
        if not started:
            print("Car is already stopped...")
        else:
            started = False
            print("Car stopped...")
    elif command == 'quit':
        print("Bye...")
        break
    else:
        print("I don't understand that...")
    previous_command = command
