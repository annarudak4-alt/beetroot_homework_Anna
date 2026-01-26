"""Завдання 2
Написання тестів для менеджера контексту r. Візьміть свою реалізацію класу менеджера контексту із Завдання 1
та напишіть для неї тести. Намагайтеся охопити якомога більше випадків
використання, позитивних, коли файл існує і все працює належним чином.
А також пишіть тести, коли ваш клас викликає помилки або у вас є помилки в наборі контекстів виконання."""

import unittest
from Task1 import FileContextManager  # імпортуємо ваш клас

class TestFileContextManager(unittest.TestCase):

    def test_write_and_read(self):
        """Перевірка: запис і читання з файлу."""
        # створюємо файл і записуємо в нього текст
        with FileContextManager("test.txt", "w") as f:
            f.write("Привіт")

        # читаємо те саме через наш контекстний менеджер
        with FileContextManager("test.txt", "r") as f:
            content = f.read()

        # перевіряємо, що зчитаний текст співпадає
        self.assertEqual(content, "Привіт")

    def test_file_closed_after_exit(self):
        """Перевірка: файл автоматично закривається після виходу з блоку with."""
        manager = FileContextManager("test.txt", "w")
        with manager as f:
            f.write("Hello!")
        # після виходу з with файл повинен бути закритий
        self.assertTrue(f.closed)

    def test_error_inside_with_block(self):
        """Перевірка: файл закривається навіть якщо виникла помилка."""
        manager = FileContextManager("test.txt", "w")
        try:
            with manager as f:
                f.write("Error test")
                raise ValueError("Тестова помилка")
        except ValueError:
            pass  # помилку очікуємо, тому ігноруємо її

        # файл має бути закритий навіть після помилки
        self.assertTrue(f.closed)

    def test_read_nonexistent_file(self):
        """Перевірка: спроба відкрити неіснуючий файл викликає помилку."""
        with self.assertRaises(FileNotFoundError):
            with FileContextManager("no_file.txt", "r") as f:
                f.read()

if __name__ == "__main__":
    unittest.main()
