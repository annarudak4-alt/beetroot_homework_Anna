"""
Запити з використанням багатопоточності
Завантажте всі коментарі з вибраного вами сабреддиту, використовуючи
URL-адресу: https://api.pushshift.io/reddit/comment/search/.
В результаті, зберігайте всі коментарі в хронологічному порядку в JSON
та виводьте їх у файл. Для цього завдання використовуйте Threads для здійснення запитів до API Reddit.
"""

import requests
import threading
import json
import time

BASE_URL = "https://api.pushshift.io/reddit/comment/search/"
SUBREDDIT = "python"
LIMIT = 100

comments = []
lock = threading.Lock()

def fetch_comments(before_timestamp):
    """Функція, яка завантажує коментарі до певного часу"""
    params = {
        "subreddit": SUBREDDIT,
        "size": LIMIT,
        "before": before_timestamp
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json().get("data", [])

    with lock:
        comments.extend(data)
    print(f"Завантажено {len(data)} коментарів")
    return data

def main():
    threads = []
    current_time = int(time.time())

    # Створюємо 3 потоків (3 запитів)
    for _ in range(3):
        thread = threading.Thread(
            target=fetch_comments,
            args=(current_time,)
        )
        threads.append(thread)
        thread.start()
        current_time -= 60 * 60  # 1 година

    # Чекаємо завершення всіх потоків
    for thread in threads:
        thread.join()
    comments.sort(key=lambda x: x["created_utc"])

    # Запис у JSON-файл
    with open("comments.json", "w", encoding="utf-8") as file:
        json.dump(comments, file, ensure_ascii=False, indent=4)
    print(f"Усього збережено {len(comments)} коментарів у comments.json")

if __name__ == "__main__":
    main()