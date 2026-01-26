"""
Завдання 1 Robots.txt Завантажте та збережіть у файл
robots.txt з Вікіпедії, веб-сайтів Twitter тощо.
"""

import requests

url = "https://www.wikipedia.org/robots.txt"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
print("HTTP статус:", response.status_code)
if response.status_code == 200:
    with open("robots.txt", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Файл robots.txt успішно збережено")
else:
    print("Не вдалося завантажити файл")