"""
Завдання 2
Використовуючи пошук в ширину, напишіть алгоритм, який може визначити
найкоротший шлях від кожної вершини до кожної іншої вершини.
Це називається задачею пошуку найкоротшого шляху для всіх пар.
"""

def bfs(graph, start):
    visited = {start}
    distance = {v: float('inf') for v in graph}
    distance[start] = 0
    queue = [start]  # список використовується як черга
    while queue:
        v = queue.pop(0)  # видаляємо перший елемент
        for u in graph[v]:
            if u not in visited:
                visited.add(u)
                distance[u] = distance[v] + 1
                queue.append(u)
    return distance

# Найкоротший шлях для всіх пар
def all_pairs_shortest_path(graph):
    return {v: bfs(graph, v) for v in graph}

graph = {
    0: [2, 3],
    1: [1, 2, 4],
    2: [0, 1, 3],
    3: [1, 2, 3],
    4: [4]
}

all_dist = all_pairs_shortest_path(graph)

print("Найкоротші відстані між усіма парами вершин:")
for start in all_dist:
    print(f"Від вершини {start}: {all_dist[start]}")