"""Завдання 2

Бібліотека
Напишіть структуру класу, яка реалізує бібліотеку. Класи:
1) Бібліотека - назва, книги = [], автори = []
2) Книга - назва, рік, автор (автор має бути екземпляром класу Автор)
3) Автор - ім'я, країна, день народження, книги = []
Бібліотечний клас
Методи:
- new_book(name: str, year: int, author: Автор) - повертає екземпляр класу Book та додає книгу до списку книг для поточної бібліотеки.
- group_by_author(author: Автор) - повертає список усіх книг, згрупованих за вказаним автором
- group_by_year(year: int) - повертає список усіх книг, згрупованих за вказаним роком
Усі 3 класи повинні мати читабельні методи __repr__ та __str__.
Також клас book повинен мати змінну класу, яка містить кількість усіх існуючих книг"""

class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []  # список книг, які написав автор

    def __repr__(self):
        return f"Author({self.name!r}, {self.country!r}, {self.birthday!r})"

    def __str__(self):
        return f"{self.name} ({self.country}, {self.birthday})"


class Book:
    total_books = 0  # змінна класу — лічильник усіх створених книг

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author

        author.books.append(self) # Додаємо книгу до списку книг автора

        Book.total_books += 1 # Збільшуємо загальний лічильник книг

    def __repr__(self):
        return f"Book({self.name!r}, {self.year!r}, {self.author.name!r})"

    def __str__(self):
        return f"«{self.name}» ({self.year}), автор: {self.author.name}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []   # усі книги бібліотеки
        self.authors = [] # усі автори бібліотеки

    def new_book(self, name: str, year: int, author: Author): #Створює нову книгу, додавання її в бібліотеку та повертає екземпляр Book
        book = Book(name, year, author)
        self.books.append(book)

        # якщо автора ще нема в бібліотеці — додаємо
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author: Author): #Повертає список усіх книг конкретного автора
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int): #Повертає список усіх книг певного року
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library({self.name!r})"

    def __str__(self):
        return f"Бібліотека: {self.name}, книг: {len(self.books)}, авторів: {len(self.authors)}"

fadden = Author("Фріда Мак-Фадден", "США", "01.05.1980")
sparks = Author("Ніколас Спаркс", "США", "31.12.1965")

# створюємо бібліотеку
lib = Library("Сучасна бібліотека")

# додаємо книги
lib.new_book("Служниця", 2023, fadden)
lib.new_book("Секрет служниці", 2024, fadden)
lib.new_book("Щоденник пам'яті", 1994, sparks)


print(lib)
print("Книги Фріди Мак-Фадден:", lib.group_by_author(fadden))
print("Книги 2023 року:", lib.group_by_year(2023))
print("Загальна кількість книг:", Book.total_books)