"""
Запити з використанням asyncio та aiohttp
Завантажте всі коментарі з вибраного вами сабреддиту, використовуючи
URL-адресу: https://api.pushshift.io/reddit/comment/search/.
В результаті, зберігайте всі коментарі в хронологічному порядку в JSON та виводьте їх у файл.
Для цього завдання використовуйте бібліотеки asyncio та aiohttp для здійснення запитів до Reddit API.
"""
import asyncio
import aiohttp
import json
import time

BASE_URL = "https://api.pushshift.io/reddit/comment/search/"
SUBREDDIT = "python"
LIMIT = 200

async def fetch_comments(session, before_timestamp):
    """Асинхронно отримує коментарі до певного часу"""
    params = {
        "subreddit": SUBREDDIT,
        "size": LIMIT,
        "before": before_timestamp
    }
    headers = {"User-Agent": "Mozilla/5.0 (asyncio example)"}

    try:
        async with session.get(BASE_URL, params=params, headers=headers) as resp:
            if resp.status != 200:
                print(f"HTTP {resp.status} – пропускаємо запит")
                return []
            data = await resp.json()
            return data.get("data", [])
    except Exception as e:
        print("Помилка запиту:", e)
        return []

async def main():
    now = int(time.time())
    # Створюємо 4 часових міток для прикладу (останні 4 годин)
    timestamps = [now - i * 3600 for i in range(4)]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_comments(session, ts) for ts in timestamps]
        results = await asyncio.gather(*tasks)

    # Об'єднуємо всі коментарі
    all_comments = [comment for batch in results for comment in batch]

    # Сортуємо хронологічно
    all_comments.sort(key=lambda x: x["created_utc"])

    # Зберігаємо у JSON
    with open("comments_async.json", "w", encoding="utf-8") as f:
        json.dump(all_comments, f, ensure_ascii=False, indent=4)

    print(f"Коментарів збережено: {len(all_comments)}")

if __name__ == "__main__":
    asyncio.run(main())