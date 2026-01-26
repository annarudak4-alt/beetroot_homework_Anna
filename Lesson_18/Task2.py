"""
Реалізуйте 2 класи, перший - Бос, а другий - Працівник.
Працівник має властивість 'boss', а її значення має бути екземпляром Boss.
Ви можете перепризначити це значення, але вам слід перевірити, чи нове значення є Boss.
Кожен Boss має список своїх власних працівників. Вам слід реалізувати метод, який
дозволяє додавати працівників до Boss. Вам не дозволено додавати екземпляри класу
Boss до списку працівників безпосередньо через доступ до атрибута, натомість використовуйте
геттери та сеттери! Ви можете рефакторингувати існуючий код.
id_ - це просто випадкове унікальне ціле число
id_ - is just a random unique integer
class Boss:
def __init__(self, id_: int, name: str, company: str):
self.id = id_ self.name = name
self.company = company
self.workers = []
class Worker:
def __init__(self, id_: int, name: str, company: str, boss: Boss):
self.id = id_ self.name = name
self.company = company
self.boss = boss
"""

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []  # список працівників

    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            if worker not in self._workers:
                self._workers.append(worker)
                worker.boss = self
        else:
            raise TypeError("Можна додавати тільки екземпляри класу Worker")


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss  # використовуємо сетер

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if not isinstance(new_boss, Boss):
            raise TypeError("boss повинен бути екземпляром класу Boss")
        # якщо працівник мав босса — видаляємо його зі старого списку
        if self._boss is not None and self in self._boss.workers:
            self._boss.workers.remove(self)
        self._boss = new_boss
        # додавання нового босса до списку
        if self not in new_boss.workers:
            new_boss.workers.append(self)

boss1 = Boss(1, "Alex", "Beetroot")
boss2 = Boss(2, "Masha", "GoIT")

worker1 = Worker(101, "Olga", "Beetroot", boss1)
worker2 = Worker(102, "Roman", "Beetroot", boss1)

print([w.name for w in boss1.workers])
boss2.add_worker(worker1)

print([w.name for w in boss1.workers])
print([w.name for w in boss2.workers])