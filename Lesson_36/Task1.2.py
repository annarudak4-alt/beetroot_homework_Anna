
import asyncio
import time
from multiprocessing import Pool

def fibonacci_sync(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def factorial_sync(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def square_sync(n):
    return n * n

def cube_sync(n):
    return n * n * n
def multiprocessing_main():
    numbers = list(range(1, 11))

    start = time.perf_counter()

    with Pool() as pool:
        fibs = pool.map(fibonacci_sync, numbers)
        facts = pool.map(factorial_sync, numbers)
        squares = pool.map(square_sync, numbers)
        cubes = pool.map(cube_sync, numbers)

    elapsed = time.perf_counter() - start

    return fibs, facts, squares, cubes, elapsed


if __name__ == "__main__":
    mp_fibs, mp_facts, mp_squares, mp_cubes, mp_time = multiprocessing_main()

    print("MULTIPROCESSING")
    print("Fibonacci:", mp_fibs)
    print("Factorial:", mp_facts)
    print("Squares:", mp_squares)
    print("Cubes:", mp_cubes)
    print(f"Час виконання: {mp_time:.6f} сек")