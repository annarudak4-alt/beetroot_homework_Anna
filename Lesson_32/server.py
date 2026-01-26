import socket

# Створюємо UDP-сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP-адреса і порт сервера
server_address = ("127.0.0.1", 12345)

# Прив'язуємо сокет до адреси
server_socket.bind(server_address)

print("UDP сервер запущено. Очікуємо повідомлення...")

while True:
    # Отримуємо повідомлення від клієнта
    data, client_address = server_socket.recvfrom(1024)

    message = data.decode("utf-8")
    print(f"Отримано від клієнта {client_address}: {message}")

    # Відповідь клієнту
    response = "Повідомлення отримано!"
    server_socket.sendto(response.encode("utf-8"), client_address)