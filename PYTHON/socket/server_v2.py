
import socket
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from Logs import server_log, server_error, server_warning, server_debug, server_critical


HOST = '127.0.0.1'
PORT = 6000

# MONGO DB CONFIGURATION
database_name = 'test_python_db'
Collection1 = 'empresa'
Collection2 = 'personajes'
Collection3 = 'lenguajes'

class MongoDB():
    def __init__(self, db_name=database_name):
        print("Iniciando conexión a MongoDB...")
        try:
            self.client = MongoClient()
            self.db = self.client[db_name]

            print("Se ha conectado con MongoDB")
            
            # TODO: GESTIONAR COMANDOS DEL CLIENTE
            # * Comandos: insertar nuevo elemento y buscar elemento
            

            


        except Exception as e:
            server_error(f"Se ha producido un error: {e}")
            print(f"Se ha producido un error: {e}")



# Clase para manejar el servidor
class Server():
    def __init__(self): # Inicialización del servidor de mongo y el socket
        self.mongo = MongoClient('mongodb://localhost:27017/')
        self.s = None
    
    def start(self):
        if not self.mongo:
            server_error("No se pudo conectar a la base de datos MongoDB.")
            return
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind((HOST, PORT))
            self.s.listen(5)  # Listen for up to 5 connections
            self.s.settimeout(60)  # Set a timeout of 60 seconds for accepting connections
            server_log("Servidor iniciado y escuchando en {}:{}".format(HOST, PORT))
            print("Servidor iniciado y escuchando en {}:{}".format(HOST, PORT))
            while True:
                add, conn = self.s.accept()
                server_log("Conexión aceptada desde: {}".format(add))
                

        except Exception as e:
            server_error("Error al iniciar el servidor: {}".format(e))
            print("Error al iniciar el servidor: {}".format(e))


if __name__ == "__main__":
    server = Server()
    server.start()