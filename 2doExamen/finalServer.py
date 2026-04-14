# INTEGRANTES DEL DÚO
# - Barajas Pacheco Harol Fabian
# - Flores Aguilera Jorge Alexei

import socket
import select
import time

HOST = "localhost"
PORT = 5000


def iniciar_servidor(max_clientes: int):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORT))
    servidor.listen(100)
    print(f"Servidor escuchando en {HOST}:{PORT}")
    print(f"Límite de conexiones simultáneas: {max_clientes}")

    entradas = [servidor]

    try:
        while True:
            clientes_activos = len(entradas) - 1

            if clientes_activos >= max_clientes:
                vigilar = [sock for sock in entradas if sock != servidor]
            else:
                vigilar = entradas[:]

            listos, _, _ = select.select(vigilar, [], [])

            for sock in listos:
                if sock is servidor:
                    conn, addr = servidor.accept()
                    entradas.append(conn)
                else:
                    try:
                        datos = sock.recv(1024)
                    except ConnectionResetError:
                        datos = None

                    if not datos:
                        entradas.remove(sock)
                        sock.close()
                    else:
                        time.sleep(0.05)

                        try:
                            sock.sendall(b"OK\n")
                        except:
                            pass

    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario.")
    finally:
        servidor.close()


if __name__ == "__main__":
    try:
        clientes = int(input("Ingrese la cantidad máxima de clientes a aceptar: "))
        iniciar_servidor(clientes)
    except ValueError:
        print("Por favor, ingrese un número válido.")