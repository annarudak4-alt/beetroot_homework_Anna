"""
Спеціальний виняток
Створіть власний виняток з назвою «CustomException».
Ви можете успадкувати його від базового класу Exception,
але розширити його функціональність, щоб записувати кожне
повідомлення про помилку у файл з назвою «logs.txt». 
Поради: Використовуйте метод __init__ для розширення функціональності
збереження повідомлень у файл.

"""

class CustomException(Exception):
    def __init__(self, msg):  
        super().__init__(msg)

        with open("logs.txt", "a", encoding="utf-8") as file: # Зберігаємо повідомлення у файл "logs.txt"
            file.write(msg + "\n")
try:
    raise CustomException("Некоректне значення!")
except CustomException as e:
    print(f"Виникла помилка: {e}")