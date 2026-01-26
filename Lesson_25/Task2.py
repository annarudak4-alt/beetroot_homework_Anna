"""
Завдання 2
Реалізуйте стек за допомогою однозв'язного списку.
"""

class Node:
    """Вузол однозв'язного списку"""
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """Стек на основі однозв'язного списку (LIFO)"""
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        """Додати елемент у стек (вставка у голову списку)"""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Видалити елемент з вершини"""
        if self.is_empty():
            raise IndexError("pop із пустого стеку")

        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        """Повернути верхній елемент без видалення"""
        if self.is_empty():
            raise IndexError("порожній стек")
        return self.top.data

    def __repr__(self):
        items = []
        cur = self.top
        while cur:
            items.append(str(cur.data))
            cur = cur.next
        return "Top -> " + " -> ".join(items)

s = Stack()

s.push(10)
s.push(15)
s.push(20)
print("Після push:", s)
print("peek =", s.peek())
print("pop =", s.pop())
print("Після pop:", s)
s.push(25)
print("Після вставки 25:", s)