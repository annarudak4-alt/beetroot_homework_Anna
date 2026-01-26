"""Напишіть декоратор, який виводить функцію з переданими їй аргументами.
ПРИМІТКА! Слід вивести функцію, а не результат її виконання!"""

def logger(func):
    def wrapper(*args, **kwargs):
        # Виведення функції
        print(func, "called with", args, kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]
add(56, 678)
square_all(1, 2, 3)




