"""
Завдання 3
Додаток «Погода»
Напишіть консольний застосунок, який приймає на вхід назву міста та повертає поточну
погоду у вибраному вами форматі. Для поточного завдання ви можете вибрати будь-який
API погоди чи вебсайт, або скористатися openweathermap.org.
"""

import requests

API_KEY = "f6a0f9eeffdd6c1ba242dd27b7ae0c94"
city = input("Назва міста: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric",
    "lang": "uk"
}

response = requests.get(url, params=params)

if response.status_code != 200:
    print("Помилка запиту")
    print("HTTP код:", response.status_code)
    print("Відповідь сервера:")
    print(response.text)
else:
    data = response.json()

    print("\nМісто:", data["name"])
    print("Температура:", data["main"]["temp"], "°C")
    print("Вологість:", data["main"]["humidity"], "%")
    print("Погода:", data["weather"][0]["description"])