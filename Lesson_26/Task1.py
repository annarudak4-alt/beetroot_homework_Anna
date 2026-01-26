"""
Завдання 1
Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.
Прочитайте про пошук Фібоначчі та імплементуйте його за допомогою Python.
Визначте складність алгоритму та порівняйте його з бінарним пошуком
"""

def binary_search_recursive(arr, target, left, right):
    # Базовий випадок: елемента немає
    if left > right:
        return -1

    mid = (left + right) // 2

    # Якщо знайдено
    if arr[mid] == target:
        return mid

    # Якщо шуканий елемент менший — йдемо в ліву половину
    if target < arr[mid]:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        # Інакше — у праву
        return binary_search_recursive(arr, target, mid + 1, right)

arr = [0,1,1,2,3,5,8,13,21,34]
print(binary_search_recursive(arr, 8, 0, len(arr)-1))

"""
Пошук Фібоначчі 
"""
def fibonacci_search(arr, target):
    n = len(arr)

    # Початкові числа Фібоначчі
    fib2 = 0         # F(k-2)
    fib1 = 1         # F(k-1)
    fib = fib1 + fib2  # F(k)

    # Знаходимо найменше число Фібоначчі >= n
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    # Позначка для відсування індексів
    offset = -1

    while fib > 1:
        # Обчислюємо індекс для порівняння
        i = min(offset + fib2, n - 1)

        # Якщо arr[i] < target — шукаємо справа
        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        # Якщо arr[i] > target — шукаємо зліва
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1

        else:
            return i  # Знайдено

    # Перевірка останнього можливого елемента
    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1
arr = [0,1,1,2,3,5,8,13,21,34]
print(fibonacci_search(arr, 8))
