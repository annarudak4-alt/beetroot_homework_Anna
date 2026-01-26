"""
Напишіть декоратор 'arg_rules', який перевіряє аргументи, передані функції.
Декоратор повинен приймати 3 аргументи:
max_length: 15
type_: str
contains: [] список символів, які має містити аргумент
Якщо деякі з перевірок правил повертають False, функція повинна
повернути False та вивести причину невдачі; інакше повернути результат.
"""

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            arg = args[0]  # функція приймає лише один основний аргумент

            if not isinstance(arg, type_):  # Перевірка типу
                print(f"Помилка: аргумент має бути типу {type_.__name__}")
                return False

            if len(arg) > max_length:    # Перевірка довжини
                print(f"Помилка: довжина аргументу перевищує {max_length}")
                return False

            for item in contains:
                if item not in arg:
                    print(f"Помилка: аргумент повинен містити '{item}'")
                    return False

            return func(*args, **kwargs)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

print(create_slogan('S@SH05'))