import socket

# Створюємо UDP-сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Адреса сервера
server_address = ("127.0.0.1", 12345)

# Повідомлення для сервера
message = "Привіт, сервер!"

# Надсилаємо повідомлення
client_socket.sendto(message.encode("utf-8"), server_address)

# Отримуємо відповідь від сервера
data, server = client_socket.recvfrom(1024)

print("Відповідь сервера:", data.decode("utf-8"))

# Закриваємо сокет
client_socket.close()