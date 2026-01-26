"""
Завдання 1

Створіть власну реалізацію вбудованої функції enumerate з назвою
'with_index', яка приймає два параметри: 'iterable' та 'start',
значення за замовчуванням дорівнює 0. Поради: див. документацію до функції enumerate

"""

def with_index(iterable, start=0):
    index = start

    for item in iterable:
        yield index, item
        index += 1

for i, value in with_index(["перший", "другий", "третій"], start=1):
    print(i, value)