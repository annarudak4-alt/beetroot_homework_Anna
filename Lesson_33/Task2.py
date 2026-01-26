"""
Завантаження даних
Завантажте всі коментарі з вибраного вами сабреддиту, використовуючи URL-адресу: https://jsonplaceholder.typicode.com/ .
В результаті, зберігайте всі коментарі в хронологічному порядку в JSON та виводьте їх у файл.
"""
import requests
import json

# URL з коментарями
url = "https://jsonplaceholder.typicode.com/comments"

# Надсилаємо запит
response = requests.get(url)

# Перевіряємо, чи успішний запит
if response.status_code == 200:
    comments = response.json()

    # Сортуємо коментарі за id (хронологічний порядок)
    comments_sorted = sorted(comments, key=lambda x: x["id"])

    # Записуємо у JSON-файл
    with open("comments.json", "w", encoding="utf-8") as file:
        json.dump(comments_sorted, file, ensure_ascii=False, indent=4)

    print("Коментарі збережено у comments.json")
else:
    print("Помилка завантаження даних")