def first_function():
    message = "Посилання з першої функції"
    def second_function():
        print(message)

    return second_function

ours_function = first_function()

ours_function()