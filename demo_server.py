""" Used for Checking the main.py and how it affects socket connections """

import socket

server_ip = "0.0.0.0"
server_port = 9900


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            print("Reached. No data sent")
            break
        print(f"Received data: {data.decode()}")


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen()
    print(f"Listening on {server_ip}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        handle_client(client_socket)


if __name__ == "__main__":
    main()
