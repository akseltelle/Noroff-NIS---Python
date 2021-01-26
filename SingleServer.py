import socket

HOST = "127.0.0.1"
PORT = 60000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("Listening...")
    conn, addr = server.accept()
    with conn:
        print("Connected by ", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received: ", data)
            conn.sendall(b'You have been successfully connected')
