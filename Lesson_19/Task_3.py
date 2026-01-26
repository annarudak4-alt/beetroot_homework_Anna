"""
Завдання 3
Створіть власну реалізацію ітерованого об'єкта, який можна використовувати
всередині циклу for-in. Також додайте логіку для отримання елементів за допомогою
синтаксису квадратних дужок.
"""

class MyList:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        for item in self.data:
            yield item

    def __getitem__(self, index):
        return self.data[index]

my_list = MyList(["троянда", "лілія", "фіалка"])

for flowers in my_list:
    print(flowers)

print(my_list[0])
print(my_list[2])