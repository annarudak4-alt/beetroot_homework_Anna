def oops():
    raise IndexError("This is an index error!")

def handle_error():
    try:
        oops()
    except IndexError:
        print("IndexError caught!")

handle_error()

# Якщо змінити oops() на KeyError

def oops():
   raise KeyError("This is a key error!")

def handle_error():
    try:
        oops()
    except IndexError:
        print("IndexError caught!")
handle_error()