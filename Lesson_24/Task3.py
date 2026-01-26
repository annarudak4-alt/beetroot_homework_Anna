"""
Завдання 3
Розширте стек, включивши метод під назвою get_from_stack, який шукає та повертає елемент e зі стеку.
Будь-який інший елемент повинен залишатися в стеку, дотримуючись їхнього порядку. Розглянемо випадок,
коли елемент не знайдено - викличіть ValueError з належною інформацією Message.
Розширте Чергу, включивши метод під назвою get_from_stack, який шукає та повертає елемент e з черги.
Будь-який інший елемент повинен залишатися в черзі, дотримуючись їхнього порядку. Розглянемо випадок,
коли елемент не знайдено - викличіть ValueError з належною інформацією Message
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Додає елемент у стек."""
        self.items.append(item)

    def pop(self):
        """Видаляє елемент із вершини стека."""
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
         return len(self.items) == 0

    def get_from_stack(self, e):
        """
        Шукає і повертає елемент e зі стека.
        """
        temp_stack = Stack()
        found_item = None
        # Витягуємо елементи, поки не знайдемо потрібний
        while not self.is_empty():
            item = self.pop()
            if item == e:
                found_item = item
                break
            else:
                temp_stack.push(item)

        # Повертаємо назад усі інші елементи в правильному порядку
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        return found_item

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("Початковий стек:", stack.items)
found = stack.get_from_stack(3)
print("Елемент пошуку:", found)
print("Стек після пошуку:", stack.items)
