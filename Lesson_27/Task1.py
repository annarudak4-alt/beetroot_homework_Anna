class Node:
    def __init__(self, key):
        # Ключ вузла
        self.key = key
        # Лівий нащадок
        self.left = None
        # Правий нащадок
        self.right = None

# ПОШУК В ДЕРЕВІ (рекурсивний)

def search(root, key):
    # Якщо дерево порожнє — елемент не знайдено
    if root is None:
        print(f"{key} не знайдено")
        return None

    # Якщо знайдено елемент
    if root.key == key:
        print(f"Знайдено ключ: {key}")
        return root

    # Якщо шуканий ключ більший — рухаємося праворуч
    if key > root.key:
        print(f"Порівняли {key} з {root.key}; рух праворуч")
        return search(root.right, key)

    # Якщо менший — ліворуч
    print(f"Порівняли {key} з {root.key}; рух ліворуч")
    return search(root.left, key)

# ВСТАВКА НОВОГО ВУЗЛА У ДЕРЕВО ПОШУКУ

def insert(root, key):
    # Якщо прийшли до порожнього місця — створюємо новий вузол
    if root is None:
        return Node(key)

    # Вставляємо в ліве піддерево
    if key < root.key:
        root.left = insert(root.left, key)
    # Вставляємо в праве піддерево
    else:
        root.right = insert(root.right, key)

    return root

## ВИДАЛЕННЯ ПІДДЕРЕВА

def delete_subtree(root, key):
    # Якщо дерево порожнє
    if root is None:
        return None

    # Якщо вузол для видалення знаходиться в лівому піддереві
    if key < root.key:
        root.left = delete_subtree(root.left, key)
        return root

    # Якщо у правому
    elif key > root.key:
        root.right = delete_subtree(root.right, key)
        return root

    # Знайдено вузол, піддерево якого треба видалити
    print(f"Видалення піддерева з коренем у вузлі: {root.key}")
    return None  # повертаємо None, видаляючи весь піддерево


# Створення дерева
root = Node(9)
root.left = Node(4)
root.right = Node(13)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(19)

print("\n--- ПОШУК ІСНУЮЧОГО ЕЛЕМЕНТА ---")
search(root, 7)

print("\n--- ПОШУК НЕІСНУЮЧОГО ЕЛЕМЕНТА ---")
search(root, 56)

print("\n--- ВСТАВКА НОВИХ ЕЛЕМЕНТІВ ---")
root = insert(root, 9)
root = insert(root, 25)

print("\n--- ВИДАЛЕННЯ ПІДДЕРЕВА (ключ = 4) ---")
root = delete_subtree(root, 4)

print("\n--- ПОШУК ПІСЛЯ ВИДАЛЕННЯ ---")
result = search(root, 4)