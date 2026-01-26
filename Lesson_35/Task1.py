"""
Прості числа
У нас є наступний вхідний список чисел, деякі з яких є простими. Вам потрібно створити корисну функцію,
яка приймає на вхід число та повертає логічне значення, незалежно від того, просте воно чи ні.
Використовуйте ThreadPoolExecutor та ProcessPoolExecutor для створення різних одночасних реалізацій фільтрації ЧИСЕЛ.
Порівняйте результати та продуктивність кожного з них.
"""
import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

#Вхідні дані
NUMBERS = [
    2,
    1099726899285419,
    1570341764013157,
    1637027521802551,
    1880450821379411,
    1893530391196711,
    2447109360961063,
    3,
    2772290760589219,
    3033700317376073,
    4350190374376723,
    4350190491008389,
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,
]

#Функції
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def filter_primes(executor_class, numbers):
    start = time.perf_counter()
    with executor_class() as executor:
        results = list(executor.map(is_prime, numbers))
    primes = [n for n, r in zip(numbers, results) if r]
    return primes, time.perf_counter() - start

#Запуск
if __name__ == "__main__":
    thread_primes, thread_time = filter_primes(ThreadPoolExecutor, NUMBERS)
    process_primes, process_time = filter_primes(ProcessPoolExecutor, NUMBERS)
    print("Threads:", thread_primes, thread_time)
    print("Processes:", process_primes, process_time)