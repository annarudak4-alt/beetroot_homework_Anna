"""
Завдання 1
Розширити несортований список
Реалізуйте методи append, index, pop, insert для UnsortedList.
Також реалізуйте метод slice, який прийматиме два параметри
'start' та 'stop' та повертатиме копію списку, починаючи з позиції та до позиції stop, але не включаючи її.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UnsortedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        """Додати в кінець списку"""
        new = Node(item)
        if self.head is None:
            self.head = new
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new

    def index(self, item):
        """Повернути позицію елемента"""
        cur = self.head
        pos = 0
        while cur:
            if cur.data == item:
                return pos
            cur = cur.next
            pos += 1
        raise ValueError("Елемент не знайдено")

    def pop(self, index):
        """Видалити за індексом і повернути значення"""
        if index == 0:
            value = self.head.data
            self.head = self.head.next
            return value

        cur = self.head
        pos = 0
        while cur and pos < index - 1:
            cur = cur.next
            pos += 1

        value = cur.next.data
        cur.next = cur.next.next
        return value

    def insert(self, index, item):
        """Вставити елемент за індексом"""
        new = Node(item)
        if index == 0:
            new.next = self.head
            self.head = new
            return

        cur = self.head
        pos = 0
        while cur and pos < index - 1:
            cur = cur.next
            pos += 1

        new.next = cur.next
        cur.next = new

    def slice(self, start, stop):
        """Повернути копію списку з діапазону [start, stop)"""
        new_list = UnsortedList()
        cur = self.head
        pos = 0
        while cur and pos < stop:
            if pos >= start:
                new_list.append(cur.data)
            cur = cur.next
            pos += 1
        return new_list

ul = UnsortedList()

ul.append(10)
ul.append(15)
ul.append(20)

print("Після append:", ul)
print("index(30) =", ul.index(15))
ul.insert(1, 15)
print("Після insert(1, 15):", ul)
print("pop(2) =", ul.pop(2))
print("Після pop:", ul)
sl = ul.slice(1, 3)
print("slice(1, 3):", sl)

