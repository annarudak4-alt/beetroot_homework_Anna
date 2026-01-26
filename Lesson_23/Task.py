from typing import List, Tuple

# O(n²)
def question1(a: List[int], b: List[int]) -> List[int]:
    return [x for x in a if x in b]  # вкладений цикл перевірки "in"

# O(1)
def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n

# O(n²)
def question3(a: List[int], b: List[int]) -> List[int]:
    res = a[:]
    for x in b:
        if x not in res:
            res.append(x)
    return res

# O(n)
def question4(lst: List[int]) -> int:
    res = 0
    for x in lst:
        if x > res:
            res = x
    return res

# O(n²)
def question5(n: int) -> List[Tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(n)]

# O(log n)
def question6(n: int) -> int:
    while n > 1:
        n //= 2
    return n