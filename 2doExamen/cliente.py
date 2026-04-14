#INTEGRANES DEL DÚO
# - Barajas Pacheco Harol Fabian
# - Flores Aguilera Jorge Alexei

import socket
import time

HOST = "localhost"
PORT = 5000


def enviarmensajes():
    print("Iniciando Fase A, enviando lsa 100 peticiones...")
    start_time = time.time()

    for i in range(100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((HOST, PORT))
        mensaje = f"DATO_SENSOR_{i:02d}_" + ("X" * 50)
        s.sendall(mensaje.encode())
        try:
            s.recv(1024)
        except Exception:
            pass

        s.close()

    tiempo_total = time.time() - start_time

    print("\n--- MÉTRICAS DE LA PRIMERA FASE ---")
    print(f"Total de peticiones: 100")
    print(f"Tiempo de ejecución: {tiempo_total:.4f} segundos")


if __name__ == "__main__":
    enviarmensajes()