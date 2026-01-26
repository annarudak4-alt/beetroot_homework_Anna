"""
Завдання 2
Echo-сервер з потоками
Створіть сервер socket echo, який обробляє кожне з'єднання в окремому потоку.
"""
import socket
import threading

def handle_client(client_socket, client_address):
    """Функція для обробки одного клієнта"""
    print(f"Підключився клієнт: {client_address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break  # клієнт закрив з'єднання

        print(f"Отримано від {client_address}: {data.decode()}")
        client_socket.sendall(data)  # echo — відправляємо назад

    print(f"Клієнт {client_address} відключився")
    client_socket.close()

def start_server():
    host = "127.0.0.1"
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Echo-сервер запущено на {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()

        # Створення нового потоку для кожного клієнта
        client_thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_address)
        )
        client_thread.start()

if __name__ == "__main__":
    start_server()