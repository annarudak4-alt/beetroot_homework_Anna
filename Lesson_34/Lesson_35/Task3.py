"""
Echo-сервер з багатопроцесорною обробкою Створіть socket echo-сервер,
який оброблятиме кожне з'єднання за допомогою бібліотеки багатопроцесорної обробки.
"""

import socket
import multiprocessing

def handle_client(conn, addr):
    """Обробка одного клієнта в окремому процесі"""
    print(f"Клієнт підключився: {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break  # клієнт закрив з'єднання
        print(f"Отримано від {addr}: {data.decode()}")
        conn.sendall(data)  # echo
    print(f"Клієнт {addr} відключився")
    conn.close()

def start_server():
    host = "0.0.0.0"   # приймати підключення з будь-якої адреси
    port = 6000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Echo-сервер запущено на {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        # Створюємо окремий процес для кожного клієнта
        process = multiprocessing.Process(
            target=handle_client,
            args=(conn, addr)
        )
        process.start()
        # Основний процес закриває копію сокета
        conn.close()

if __name__ == "__main__":
    start_server()