
import asyncio
import time

async def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

async def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

async def square(n):
    return n * n

async def cube(n):
    return n * n * n

async def async_main():
    numbers = list(range(1, 11))

    start = time.perf_counter()

    fibs = await asyncio.gather(*(fibonacci(n) for n in numbers))
    facts = await asyncio.gather(*(factorial(n) for n in numbers))
    squares = await asyncio.gather(*(square(n) for n in numbers))
    cubes = await asyncio.gather(*(cube(n) for n in numbers))
    elapsed = time.perf_counter() - start
    return fibs, facts, squares, cubes, elapsed

if __name__ == "__main__":
    fibs, facts, squares, cubes, async_time = asyncio.run(async_main())

    print("ASYNCIO")
    print("Fibonacci:", fibs)
    print("Factorial:", facts)
    print("Squares:", squares)
    print("Cubes:", cubes)
    print(f"Час виконання: {async_time:.6f} сек\n")