import socket

HOST = "127.0.0.1"
PORT = 60000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    print("Connecting...")
    client.connect((HOST, PORT))
    client.sendall(b'Hello World!')
    data = client.recv(1024)

print("Received: ", data)
