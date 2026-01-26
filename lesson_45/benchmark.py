import httpx
import time
import asyncio


async def benchmark_async():
    total_start = time.perf_counter()
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)

    total_end = time.perf_counter()
    for i, response in enumerate(responses):
        print(f"URL: {urls[i]} | Статус: {response.status_code}")

    print(f"--- Загальний час (Async): {total_end - total_start:.4f} сек ---")

urls = [
    "http://127.0.0.1:8000/",           # Головна
    "http://127.0.0.1:8000/note/new/"
]


def benchmark_sync():
    total_start = time.perf_counter()
    for url in urls:
        start = time.perf_counter()
        with httpx.Client() as client:
            # Примітка: для доступу потрібна авторизація,
            # але ми вимірюємо час відгуку самого view (навіть редирект)
            response = client.get(url)
        end = time.perf_counter()
        print(f"URL: {url} | Час: {end - start:.4f} сек")

    total_end = time.perf_counter()
    print(f"--- Загальний час (Sync): {total_end - total_start:.4f} сек ---")


if __name__ == "__main__":
    benchmark_sync()