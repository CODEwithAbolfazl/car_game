is_started = False

while True :
    input_message = input('>').lower()

    if input_message == "start" :
        if is_started   :
            print("it's already started")
        else:
            print("car started ... ready to go!")
            is_started = True

    elif input_message == "stop" :
        if not is_started :
            print("it's already stopped")
        else:
            print("car stopped")
            is_started = False


    elif input_message == "quit" :
        break

    else:
        print("i don't understand that ...")
