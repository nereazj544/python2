import socket
from Logs import server_log, server_error, server_warning, server_debug, server_critical

# CONFIGURACIÓN DEL SERVIDOR
HOST = '127.0.0.1'
PORT = 6000

def start():
    try:
        print("Iniciando el servidor...")
        server_log("Iniciando el servidor...")
        # Código para iniciar el servidor
        server_log("Iniciando el servidor en {}:{}".format(HOST, PORT))
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(5)  # Escuchar hasta 5 conexiones entrantes
        server_log("Servidor iniciado y escuchando en {}:{}".format(HOST, PORT))
        while True:
            add, conn = server.accept()  # Aceptar una conexión entrante
            print("Conexión aceptada desde:", add)
            server_log("Conexión aceptada desde: {}".format(add))
            
            # mensajes de envio al cliente
            msg = '¡Hola, bienvenido al habla el servidor! Por favor, envie un comando de los siguientes:\n' \
            '1. Coleccion: empresa\n' \
            '2. Coleccion: persoanjes\n' \
            '3. Coleccion: lenguajes\n' \

            conn.send(msg.encode('utf-8'))
            server_log("Mensaje enviado al cliente: {}".format(msg))




    except Exception as e:
        server_error(f"Error al iniciar el servidor: {e}")

start()