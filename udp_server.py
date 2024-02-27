import socket
import os
from faker import Faker

fake = Faker()

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = "udp_socket_file"

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f"Starting up on {server_address}")

sock.bind(server_address)


while True:
    print("\nwaiting for receive message...")

    data, address = sock.recvfrom(4096)

    print(f"received {len(data)} bytes from {address}")
    print(data)

    if data:
        faker_text = fake.text()

        sent = sock.sendto(faker_text.encode("utf-8"), address)
        print(f"sent {sent} bytes to {address}.")
