import socket

HOST="192.168.56.1"
PORT=5000
BUFFER_SIZE=1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketServer:
    print(f"Servidor listo y escuchando")
    socketServer.bind((HOST, PORT))
    socketServer.listen(1)
    while True:
        conn, addr = socketServer.accept()
        while True:
        with conn:
            conn.sendall("Bienvenido al servidor".encode())
