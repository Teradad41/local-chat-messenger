import socket
import os


sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = "udp_socket_file"
client_address = "udp_client_socket_file"

try:
    os.unlink(client_address)
except FileNotFoundError:
    pass

sock.bind(client_address)

try:
    while True:
        message = input("Enter message to send: ")
        if message == "exit":
            break

        b_message = message.encode("utf-8")

        print(f"sending {b_message}.")
        sent = sock.sendto(b_message, server_address)

        print("waiting to receive...")

        data, server_address = sock.recvfrom(4096)
        print(f"\nReceived {data}.\n")

finally:
    print("\nclosing socket")
    sock.close()
