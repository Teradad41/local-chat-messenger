import socket
import os
from faker import Faker


sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = 'socket_file'

fake = Faker('ja-JP')
text = fake.text()

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f'Starting up on {server_address}')

sock.bind(server_address)
sock.listen(1)

while True:
    client_socket, client_address = sock.accept()

    try:
        while True:
            data = client_socket.recv(1024)
            decoded_data = data.decode('utf-8')

            print(f'Received {decoded_data}')

            if data:
                response = text
                client_socket.sendall(response.encode())
            else:
                print(f'No data from {client_address}')
                break
    finally:
        print('Closing current connection...')
        client_socket.close()