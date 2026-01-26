"""
Завдання 3
Один зі способів покращити швидке сортування – використовувати сортування вставками
для списків малої довжини (назвемо це "обмеженням розділення"). Чому це має сенс?
Перереалізуйте швидке сортування та використовуйте його для сортування випадкового списку цілих чисел.
Виконайте аналіз, використовуючи різні розміри списків для визначення обмеження розділення.
"""

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, left, right):
    pivot = arr[(left + right) // 2]
    i, j = left, right

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return i, j

def quicksort(arr, left, right, threshold=10):
    # якщо підмасив маленький — сортуємо вставками
    if right - left < threshold:
        insertion_sort(arr, left, right)
        return
    # інакше — класичний quicksort
    i, j = partition(arr, left, right)
    if left < j:
        quicksort(arr, left, j, threshold)
    if i < right:
        quicksort(arr, i, right, threshold)


arr = [15, 112, 86, 12, 99, 321, 43, 56, 3, 6]

print("До сортування:", arr)
quicksort(arr, 0, len(arr) - 1, threshold=10)
print("Після сортування:", arr)