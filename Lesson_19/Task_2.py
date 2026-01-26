"""
Завдання 2

Створіть власну реалізацію вбудованої функції range з назвою in_range(),
яка приймає три параметри: «start», «end» та необов'язковий крок.
Поради: Дивіться документацію до функції «range».
"""

def in_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0

    if step > 0:
        while start < end:
            yield start
            start += step
    else:
        while start > end:
            yield start
            start += step

print(list(in_range(6)))
print(list(in_range(3, 15, 2)))
print(list(in_range(20, 4, -2)))
