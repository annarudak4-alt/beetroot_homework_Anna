def divide_square():
    try:
        # Дані від користувача
        a = float(input("Введіть число a: "))
        b = float(input("Введіть число b: "))
        
        # Обчислення
        result = (a ** 2) / b
        print(f"Відповідь: {result}")

    except ValueError:
        # Користувач ввів не число
        print("Помилка: вводити тільки числа!")
        
    except ZeroDivisionError:
        #  b = нулю
        print("Помилка: на нуль ділити не можна!")

divide_square()