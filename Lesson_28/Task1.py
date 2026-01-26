"""
Завдання 1
Бульбашкове сортування можна модифікувати для "бульбашкового" сортування в обох напрямках.
Перший прохід переміщує список "вгору", а другий прохід - "вниз". Цей чергуючий шаблон продовжується,
доки більше проходів не буде потрібно. Реалізуйте цей варіант і опишіть, за яких обставин він може бути доцільним.
"""

def cocktail_shaker_sort(arr):
    # Початкові межі проходів
    left = 0
    right = len(arr) - 1
    while left < right:
        # ПРОХІД СПРАВА НАЛІВО (вгору)
        swapped = False
        for i in range(left, right):
            # Якщо сусідні елементи не впорядковані - міняємо
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        # Якщо за прохід нічого не змінилося — масив уже відсортований
        if not swapped:
            break
        right -= 1

        # ПРОХІД ЗЛІВА НАПРАВО (вниз)
        swapped = False
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        # Якщо змін не було — масив відсортований
        if not swapped:
            break
        left += 1
    return arr

nums = [15, 112, 86, 12, 99, 321]
print("До сортування:", nums)

sorted_nums = cocktail_shaker_sort(nums)
print("Після сортування:", sorted_nums)