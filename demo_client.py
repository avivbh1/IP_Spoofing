""" Used for Checking the main.py and how it affects socket connections """

import socket
server_ip = "192.168.1.106"
server_port = 9900
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

message = "Hello, server!"
client_socket.send(message.encode())
response = client_socket.recv(1024)
print("Server response:", response.decode())
client_socket.close()
