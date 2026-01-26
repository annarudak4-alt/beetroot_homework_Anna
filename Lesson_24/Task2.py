"""
Завдання 2
Напишіть програму, яка зчитує послідовність символів та визначає,
чи є її дужки, фігурні дужки та фігурні дужки «збалансованими».
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Функція для перевірки збалансованості дужок
def is_balanced(sequence):
    stack = Stack()

    for char in sequence:
        if char == '(':
            stack.push(char)  # додаємо відкривну дужку
        elif char == ')':
            if stack.is_empty():  # немає пари для закривної
                return False
            stack.pop()  # видаляємо відповідну відкривну дужку

    # Якщо стек порожній — усі дужки закриті правильно
    return stack.is_empty()

sequence = "()()()"

if is_balanced(sequence):
    print("Дужки збалансовані")
else:
    print("Дужки не збалансовані")