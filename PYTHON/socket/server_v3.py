
# ! IMPORTAR LIBRERIAS
import socket
from pymongo import MongoClient
from Logs import server_critical, server_error, server_log, server_debug, server_warning


# Configuracion del servidor
HOST = '127.0.0.1'
PORT = 6000

class Server:
    print("SERVER ON")
    server_log("SERVER ENCENDIDO")
    
    # CREACION DE LAS CONEXIONES
    client = MongoClient("mongodb://localhost:27017/")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)
    s.settimeout(60) # 60 minutos
