import socket


def obtener_direccion_ipv4():
    try:
        # Obtener el nombre del host local
        hostname = socket.gethostname()

        # Obtener la dirección IPv4 asociada con el nombre del host
        direccion_ipv4 = socket.gethostbyname(hostname)

        return direccion_ipv4
    except Exception as e:
        print("Error al obtener la dirección IPv4:", str(e))
        return None


direccion_ipv4 = obtener_direccion_ipv4()
if direccion_ipv4:
    print(f"La dirección IPv4 de tu dispositivo es: {direccion_ipv4}")
