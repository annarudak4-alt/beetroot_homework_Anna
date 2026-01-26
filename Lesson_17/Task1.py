"""Завдання 1
Перевантаження методу.
Створіть базовий клас з назвою Animal та методом talk,
а потім створіть два підкласи: Dog та Cat, і зробіть їхню
власну реалізацію методу talk різною. Наприклад, Dog може
виводити «гав-гав», а Cat — «няв».
Також створіть просту узагальнену функцію, яка приймає як вхідний
екземпляр класів Cat або Dog та виконує метод talk для вхідного параметра.
"""
class Animal:
    pass

    def talk(self):
        raise NotImplementedError("Must be implemented by subclass")

class Cat(Animal):
    def talk(self):
        print("Meow!")

class Dog(Animal):
    def talk(self):
        print("Woof!")


def make_it_talk(animal: Animal):
    # Викликаємо метод talk у переданого об'єкта
    animal.talk()

dog = Dog()
cat = Cat()

make_it_talk(dog)  # Woof!
make_it_talk(cat)  # Meow!
