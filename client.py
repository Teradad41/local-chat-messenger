import socket
import sys
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = 'socket_file'
print(f'Connection to {server_address}')

fake = Faker('ja-JP')
name = fake.name()

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    while True:
        text = input('Enter >> ')

        if text == "exit":
            print('Thank you for using Local Chat Messenger.')
            sys.exit(0)

        message = f"Name: {name} Message: {text}"
        byte_message = message.encode('utf-8')
        sock.sendall(byte_message)

        data = sock.recv(1024).decode('utf-8')

        if not data:
            print('server disconnected')
            break
        else:
            print(f'Server response: {data}')

finally:
    print('Closing socket')
    sock.close()