"""
Завдання 1
Змініть «пошук у глибину», щоб отримати сильно зв'язані компоненти ( Строго зв'язані компоненти ).
"""

# DFS для першого обходу (час завершення)
def dfs_finish(graph, v, visited, stack):
    visited.add(v)
    for u in graph[v]:
        if u not in visited:
            dfs_finish(graph, u, visited, stack)
    stack.append(v)  # додаємо вершину після обходу всіх дітей

# DFS для другого обходу (збір компонент)
def dfs_collect(transpose, v, visited, component):
    visited.add(v)
    component.append(v)
    for u in transpose[v]:
        if u not in visited:
            dfs_collect(transpose, u, visited, component)

# Транспонування графа
def transpose_graph(graph):
    transpose = {}
    for v in graph:
        transpose[v] = []
    for v in graph:
        for u in graph[v]:
            transpose[u].append(v)
    return transpose

# Основна функція для SCC
def strongly_connected_components(graph):
    visited = set()
    stack = []

    # 1) Перший DFS, заповнюємо стек
    for v in graph:
        if v not in visited:
            dfs_finish(graph, v, visited, stack)

    # 2) Транспонований граф
    transpose = transpose_graph(graph)

    # 3) Другий DFS по порядку зі стеку
    visited.clear()
    scc_list = []
    while stack:
        v = stack.pop()
        if v not in visited:
            component = []
            dfs_collect(transpose, v, visited, component)
            scc_list.append(component)
    return scc_list

graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: []
}
scc = strongly_connected_components(graph)
print("Сильно звʼязані компоненти:")
for comp in scc:
    print(comp)
