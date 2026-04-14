#INTEGRANES DEL DÚO
# - Barajas Pacheco Harol Fabian
# - Flores Aguilera Jorge Alexei

import socket
import select
import time

HOST = "localhost"
PORT = 5000


def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORT))
    servidor.listen(100) #para poder escuchar las 100 peticiones casi simultaneas
    print(f"Servidor escuchando en {HOST}:{PORT}")

    entradas = [servidor]

    try:
        while True:
            listos, _, _ = select.select(entradas, [], [])

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
        print("\nServidor detenido.")
    finally:
        servidor.close()


if __name__ == "__main__":
    iniciar_servidor()
