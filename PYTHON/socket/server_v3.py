
# ! IMPORTAR LIBRERIAS
import socket
from pymongo import MongoClient
from Logs import server_critical, server_error, server_log, server_debug, server_warning


# Configuracion del servidor
HOST = '127.0.0.1'
PORT = 6000

def coleccionEmpresa(conn):
    print("COLECCION EMPRESA")
    data = conn.recv(1024).decode()
    if not data:
        server_warning("No se recibieron datos del cliente, cerrando conexión")
        return

class Server:
    def __init__(self):
        print("SERVER ON")
        server_log("SERVER ENCENDIDO")
    
        # CREACION DE LAS CONEXIONES
        self.client = MongoClient("mongodb://localhost:27017/")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))
        self.s.listen(5)
    
    server_log("Servidor iniciado y escuchando en {}:{}".format(HOST, PORT))
    print("Servidor iniciado y escuchando en {}:{}".format(HOST, PORT))

    while True:


        # mensaje del cliente

        def start(self, conn, addr):
            while True:
                conn, addr = self.s.accept()
                msg = conn.recv(1024).decode()
                print("Conexión establecida con:", addr)
                server_log("Conexión establecida con: {}".format(addr))
                if not msg:
                    server_warning("No se recibieron datos del cliente, cerrando conexión")
                    break
                server_log("Datos recibidos del cliente: {}".format(msg))
        
        # ? mensajes del cliente (opciones)
            if msg.lower() == "empresa": # Coleccion empresa
                coleccionEmpresa(conn)
                print("Opcion: Empresa")
            elif msg.lower() == "personaje": # Coleccion personaje
                # coleccionPersonaje()
                print("Opcion: Personaje")
            elif msg.lower() == "lenguajes": # Coleccion lenguajes
                print("Opcion: lenguajes")
                # coleccionLenguajes()
            else:
                msg = "NO HAS ELEGIDO UNA OPCION CORRECTA"
                server_warning("CLIENTE NO ELIGIO OPCION CORRECTA")
                break
            try:
                server_log("Iniciando el servidor...")
                Server()
            except Exception as e:
                server_critical(f"Error al iniciar el servidor: {e}")
                print(f"Error al iniciar el servidor: {e}")




