import socket
import os
from faker import Faker


fake = Faker()
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = "tcp_socket_file"

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f"Starting up on {server_address}.")

sock.bind(server_address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()

    try:
        print(f"connection from {client_address}")

        while True:
            data = connection.recv(4096)
            data_str = data.decode("utf-8")

            print(f"Received {data_str}")

            if data:
                response = fake.text()
                connection.sendall(response.encode("utf-8"))
            else:
                print(f"No data from {client_address}")
                break

    finally:
        print("closing current connection...")
        connection.close()
