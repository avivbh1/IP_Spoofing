import socket

server_ip = "0.0.0.0"
server_port = 9900


def handle_client(client_socket):
    # Handle incoming packets from the client
    while True:
        data = client_socket.recv(1024)
        if not data:
            print("Reached. No data sent")
            break
        print(f"Received data: {data.decode()}")


def main():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the IP address and port
    server_socket.bind((server_ip, server_port))

    # Listen for incoming connections
    server_socket.listen()

    print(f"Listening on {server_ip}:{server_port}")

    while True:
        # Accept an incoming connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Handle the client's packets
        handle_client(client_socket)


if __name__ == "__main__":
    main()
