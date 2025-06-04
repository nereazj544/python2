
# ! IMPORTAR LIBRERIAS
import socket
from pymongo import MongoClient
from Logs import server_critical, server_error, server_log, server_debug, server_warning


# Configuracion del servidor
HOST = 'localhost'
PORT = 1029  # Puerto del servidor

db_name = "test_python_db"  # Nombre de la base de datos
collection1 = "empresa"
collection2 = "personaje"
collection3 = "lenguajes"

def coleccionEmpresa(conn):
    print("COLECCION EMPRESA")
    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]  # Nombre de la base de datos
    collection = db[collection1] #coleccion empresa
    server_log("Conexión a la base de datos establecida")

    data = conn.recv(1024).decode()
    if not data:
        server_warning("No se recibieron datos del cliente, cerrando conexión")
        return
    #* Insetar datos en la coleccion empresa
    if data.lower() == "insertar":
        server_log("Insertando datos en la colección empresa")
        msg = "Ingrese los datos de la empresa (nombre): "
        conn.send(msg.encode())
        data = conn.recv(1024).decode()
        if not data:
            server_warning("No se recibieron datos del cliente, cerrando conexión")
            return
        msg = "Datos recibidos: {}".format(data)
        server_log(f"Se recibieron los datos: {data}")
        data = {
            'id' : collection.count_documents({}) + 1,  
            'nombre': data
        }
        nl = collection.insert_one(data)  # Insertar el nuevo documento
        server_log(f"Nuevo documento insertado con ID: {nl.inserted_id}")
        msg = "Datos insertados correctamente en la colección empresa"
        conn.send(msg.encode())
    #* Consultar datos en la coleccion empresa
    if data.lower() == "consultar":
        server_log("Consultando datos en la colección empresa")
        msg = "Ingrese el nombre de la empresa a consultar: "
        conn.send(msg.encode())
        data = conn.recv(1024).decode()
        if not data:
            server_warning("No se recibieron datos del cliente, cerrando conexión")
            return
        r = collection.find_one({'nombre': data})
        if r:
            msg = "Datos encontrados: {}".format(r)
            server_log(f"Se encontraron los datos: {r}")
            msg = "Datos encontrados: {}".format(r)
            server_log(f"Datos encontrados: {r}")
            conn.send(msg.encode())
        else:
            msg = "No se encontraron datos para la empresa: {}".format(data)
            server_warning(f"No se encontraron datos para la empresa: {data}")
        conn.send(msg.encode())


class Server:
    def __init__(self):
        print("SERVER ON")
        server_log("SERVER ENCENDIDO")
    
        # CREACION DE LAS CONEXIONES
        # self.client = MongoClient("mongodb://localhost:27017/")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))
        self.s.listen(5)
    
    server_log("Servidor iniciado y escuchando en {}:{}".format(HOST, PORT))
    print("Servidor iniciado y escuchando en {}:{}".format(HOST, PORT))

    while True:

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
                # coleccionPersonaje(conn)
                print("Opcion: Personaje")
            elif msg.lower() == "lenguajes": # Coleccion lenguajes
                # coleccionLenguajes(conn)
                print("Opcion: lenguajes")
            else:
                msg = "NO HAS ELEGIDO UNA OPCION CORRECTA"
                server_warning("CLIENTE NO ELIGIO OPCION CORRECTA")
                return
            try:
                server_log("Iniciando el servidor...")
                Server()
            except Exception as e:
                server_critical(f"Error al iniciar el servidor: {e}")
                print(f"Error al iniciar el servidor: {e}")




