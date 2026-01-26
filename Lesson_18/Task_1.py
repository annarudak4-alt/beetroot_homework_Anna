"""
Завдання 1
Створіть метод класу з назвою `validate`,
який має викликатися з методу `__init__`
для перевірки параметра email, переданого конструктору.
Логіка всередині методу `validate` може полягати в перевірці,
чи є переданий параметр email коректним рядком електронної пошти.
Підтвердження електронної пошти:
Дійсний формат адреси електронної пошти
Адреса електронної пошти

"""

class User:
    def __init__(self, email):
        self.email = email

    @classmethod
    def validate(cls, email):
        # Перевіряємо, що є символ '@' і тільки один
        if email.count('@') != 1:
            raise ValueError("Email повинен містити один символ '@'!")

        # Розділяємо на дві частини: ім'я користувача та домен
        name, domain = email.split('@')

        # Перевіряємо, що обидві частини не порожні
        if not name or not domain:
            raise ValueError("Email повинен містити частину до та після '@'!")

        # Перевіряємо, що домен містить хоча б одну крапку
        if '.' not in domain:
            raise ValueError("Домен повинен містити крапку (наприклад, gmail.com)!")

        # Перевіряємо, що крапка не стоїть в кінці
        if domain.endswith('.'):
            raise ValueError("Домен не може закінчуватись на крапку!")

        print("Email пройшов перевірку ✅")

try:
    user1 = User("example@gmail.com")   # коректний
    user2 = User("wrong_email@com")     # некоректний
except Exception as e:
    print("Помилка:", e)

