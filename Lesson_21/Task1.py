"""
Завдання 1
Клас менеджера файлового контексту
Створіть власний клас, який може поводитися як вбудована функція 'open'.
Також вам потрібно розширити його функціональність за допомогою лічильника та логування.
Зверніть особливу увагу на реалізацію методу '__exit__', який має відповідати всім вимогам
до менеджерів контексту.
"""

import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileContextManager:
    def __init__(self, filename, mode='r'):
        # Ініціалізація з іменем файлу і режимом відкриття
        self.filename = filename
        self.mode = mode
        self.file = None
        self.open_count = 0  # Лічильник відкриттів

    def __enter__(self):
        # Метод, який викликається при вході в контекстний менеджер
        self.file = open(self.filename, self.mode)  # Відкриття файлу
        self.open_count += 1  # Збільшення лічильника
        logging.info(f'Файл "{self.filename}" був відкритий. Загалом відкриттів: {self.open_count}.')
        return self.file  # Повертаємо об'єкт файлу

    def __exit__(self, exc_type, exc_value, traceback):
        # Метод, який викликається при виході з контекстного менеджера
        if self.file:
            self.file.close()  # Закриття файлу
            logging.info(f'Файл "{self.filename}" був закритий.')

# Використання нашого контекстного менеджера
if __name__ == "__main__":
    with FileContextManager("example.txt", "w") as f:
        f.write("Привіт, світ!")  # Запис у файл

    with FileContextManager("example.txt", "r") as f:
        content = f.read()  # Читання з файлу
        print(content)