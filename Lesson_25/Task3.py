"""
Завдання 3
Реалізуйте чергу, використовуючи однозв'язний список.
"""

class Node:
    """Вузол однозв'язного списку"""
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """Черга FIFO на основі однозв'язного списку"""
    def __init__(self):
        self.front = None   # початок черги
        self.rear = None    # кінець черги

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        """Додати елемент у кінець черги"""
        new_node = Node(item)

        if self.is_empty():
            # якщо черга пуста — front і rear однакові
            self.front = self.rear = new_node
        else:
            # додаємо після останнього
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Видалити елемент з початку черги"""
        if self.is_empty():
            raise IndexError("dequeue з порожньої черги")

        value = self.front.data
        self.front = self.front.next

        # якщо після видалення черга стала порожня
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        """Подивитися перший елемент"""
        if self.is_empty():
            raise IndexError("черга порожня")
        return self.front.data

    def __repr__(self):
        cur = self.front
        items = []
        while cur:
            items.append(str(cur.data))
            cur = cur.next
        return "Front -> " + " -> ".join(items) + " -> Rear"

q = Queue()

q.enqueue(10)
q.enqueue(15)
q.enqueue(20)
print("Після enqueue:", q)
print("peek =", q.peek())
print("dequeue =", q.dequeue())
print("Після dequeue:", q)
q.enqueue(25)
print("Після enqueue 25:", q)