"""
Завдання 1
Напишіть програму, яка зчитує послідовність символів та
друкує їх у зворотному порядку, використовуючи вашу реалізацію Stack.
"""

class Stack:
    def __init__(self):
        self.items = []   # Порожній список для зберігання елементів стека

    def push(self, item):
        self.items.append(item)    # Додаємо елемент у стек

    def pop(self):
        if not self.is_empty():   # Видаляємо і повертаємо останній елемент (верхівку стека)
            return self.items.pop()

    def is_empty(self):
        # Перевіряємо, чи стек порожній
        return len(self.items) == 0

stack = Stack() # Створюємо об'єкт класу Stack
sequence = "1,2,3,4,5,6,7,8,9"

# Додаємо кожен символ у стек
for char in sequence:
    stack.push(char)

# Зворотна послідовність
reversed_sequence = ""
while not stack.is_empty():
    reversed_sequence += stack.pop()

print("Послідовність у зворотному порядку:", reversed_sequence)
