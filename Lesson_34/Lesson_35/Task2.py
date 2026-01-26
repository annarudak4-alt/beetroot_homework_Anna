"""
Запити з використанням бібліотек паралельної та багатопроцесорної обробки
Завантажте всі коментарі з вибраного вами сабреддиту, використовуючи URL-адресу: https://api.pushshift.io/reddit/comment/search/ .
В результаті, зберігайте всі коментарі в хронологічному порядку в JSON та виводьте їх у файл.
Для цього завдання використовуйте бібліотеки для паралельної та багатопроцесорної обробки запитів до Reddit API.
"""
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

BASE_URL = "https://api.pushshift.io/reddit/comment/search/"
SUBREDDIT = "python"
LIMIT = 200

def fetch_comments(before_timestamp):
    headers = {
        "User-Agent": "Mozilla/5.0 (Educational project)"
    }
    params = {
        "subreddit": SUBREDDIT,
        "size": LIMIT,
        "before": before_timestamp
    }
    try:
        response = requests.get(
            BASE_URL,
            params=params,
            headers=headers,
            timeout=10
        )
        if response.status_code != 200:
            print(f"HTTP {response.status_code} – запит пропущено")
            return []
        return response.json().get("data", [])
    except requests.RequestException as e:
        print("Помилка запиту:", e)
        return []

def load_with_executor(executor_class, timestamps):
    """Завантаження коментарів з використанням executor"""
    all_comments = []
    start = time.perf_counter()
    with executor_class() as executor:
        results = executor.map(fetch_comments, timestamps)
        for batch in results:
            all_comments.extend(batch)
    elapsed = time.perf_counter() - start
    return all_comments, elapsed

if __name__ == "__main__":
    #Формуємо часові мітки (крок — 1 година)
    now = int(time.time())
    timestamps = [now - i * 3600 for i in range(5)]
    #Паралельна обробка (потоки)
    thread_comments, thread_time = load_with_executor(
        ThreadPoolExecutor, timestamps
    )
    #Багатопроцесорна обробка
    process_comments, process_time = load_with_executor(
        ProcessPoolExecutor, timestamps
    )
    #Об'єднуємо всі коментарі
    all_comments = thread_comments + process_comments
    #Сортуємо хронологічно
    all_comments.sort(key=lambda x: x["created_utc"])
    #Запис у JSON-файл
    with open("comments.json", "w", encoding="utf-8") as file:
        json.dump(all_comments, file, ensure_ascii=False, indent=4)
    print(f"Коментарів збережено: {len(all_comments)}")
    print(f"ThreadPoolExecutor: {thread_time:.2f} сек")
    print(f"ProcessPoolExecutor: {process_time:.2f} сек")