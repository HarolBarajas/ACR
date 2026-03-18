import socket

HOST="192.168.56.2"
PORT = 5000
BUFSIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketCliente:
    socketCliente.connect((HOST, PORT))
    socketCliente.send(b"Oye te estoy hablando server!\n Hazme caso")
    socketCliente.recv(BUFSIZE)