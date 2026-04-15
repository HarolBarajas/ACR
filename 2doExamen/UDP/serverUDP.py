import socket
import time

PORT = 6000


def iniciar_server(host: str):
    socketServerUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketServerUDP.bind((host, PORT))

    print(f"Servidor escuchando en {host}:{PORT} (Presiona Ctrl+C para detener)")

    contador_paquetes = 0

    try:
        while True:
            data, addr = socketServerUDP.recvfrom(1024)

            contador_paquetes += 1
            mensaje = data.decode('utf-8')
            print(f"[{contador_paquetes}] Recibido: {mensaje} desde {addr}")
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\n--- Simulación finalizada ---")
        print(f"Métrica 1: Total de paquetes recibidos: {contador_paquetes}")

    finally:
        socketServerUDP.close()


def main():
    host = input("Ingrese la dirección del server: ")
    iniciar_server(host)


if __name__ == "__main__":
    main()