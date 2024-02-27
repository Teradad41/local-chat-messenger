import socket
import sys
from faker import Faker

fake = Faker()
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = "tcp_socket_file"

print(f"connection to {server_address}.")

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    while True:
        text = input("Enter message to send: ")
        if text == "exit":
            break

        name = fake.name()
        message = f"Name: {name} Message: {text}"

        sock.sendall(message.encode("utf-8"))
        sock.settimeout(2)

        try:
            while True:
                data = str(sock.recv(4096))

                if data:
                    print("Server response: ", data)
                else:
                    break
        except TimeoutError:
            print("socket timeout, ending listening for server messages.")

finally:
    print("\nclosing socket")
    sock.close()
