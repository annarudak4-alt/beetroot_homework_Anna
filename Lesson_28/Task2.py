"""
Завдання 2
Реалізуйте функцію mergeSort без використання оператора зрізу.
"""
def merge_sort(arr, left, right):
    # Якщо в діапазоні один або нуль елементів — він уже відсортований
    if left >= right:
        return
    # Знаходимо середину
    mid = (left + right) // 2
    # Рекурсивно сортуємо ліву частину
    merge_sort(arr, left, mid)
    # Рекурсивно сортуємо праву частину
    merge_sort(arr, mid + 1, right)
    # Зливаємо дві частини
    merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    # Створюємо тимчасові масиви для лівої та правої частини
    temp = []
    i = left       # індекс для лівої половини
    j = mid + 1    # індекс для правої половини
    # Порівнюємо елементи і додаємо найменший у temp
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    # Додаємо залишки з лівої частини
    while i <= mid:
        temp.append(arr[i])
        i += 1
    # Додаємо залишки з правої частини
    while j <= right:
        temp.append(arr[j])
        j += 1
    # Переносимо відсортовані елементи назад у масив
    for k in range(len(temp)):
        arr[left + k] = temp[k]

numbers = [15, 112, 86, 12, 99, 321]
print("До сортування:", numbers)
merge_sort(numbers, 0, len(numbers) - 1)
print("Після сортування:", numbers)