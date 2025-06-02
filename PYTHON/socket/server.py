
# ! BIBLIOTECA PARA CREAR EL SERVIDOR Y CONEXION CON MONGODB

import socket
from pymongo import MongoClient
from Logs import server_log, server_error, server_warning, server_debug, server_critical

# CONFIGURACIÓN DEL SERVIDOR
HOST = '127.0.0.1'
PORT = 6000

database_name = 'test_python_db'

Collection1 = 'empresa'
Collection2 = 'personajes'
Collection3 = 'lenguajes'



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

            # RECIBIR MENSAJES DEL CLIENTE
            data = conn.recv(1024).decode()
            if not data:
                server_warning("No se recibieron datos del cliente, cerrando conexión.")
                break
            server_log("Datos recibidos del cliente: {}".format(data))
            print("Datos recibidos del cliente:", data)

            if data == 1:
                msg = 'Has seleccionado la coleccion empresa.'
                conn.send(msg.encode('utf-8'))
                server_log("Mensaje enviado al cliente: {}".format(msg))
                
                EmpresaColeccion(conn)


            elif data == 2:
                msg = 'Has seleccionado la coleccion personajes.'
                conn.send(msg.encode('utf-8'))
                server_log("Mensaje enviado al cliente: {}".format(msg))
            elif data == 3:
                msg = 'Has seleccionado la coleccion lenguajes.'
                conn.send(msg.encode('utf-8'))
                server_log("Mensaje enviado al cliente: {}".format(msg))



    except Exception as e:
        server_error(f"Error al iniciar el servidor: {e}")

start()



def EmpresaColeccion(conn):
    print("Conectando a la coleccion empresa...")
    server_log("Conectando a la coleccion empresa...")

    try:
        client = MongoClient('mongodb://localhost:27017/')
        database = client[database_name]  # Conectar a la base de datos
        collection = database[Collection1]  # Conectar a la colección 'empresa'
        server_log("Conexión a la colección 'empresa' establecida correctamente.")

        msg = 'Conexión a la colección empresa establecida correctamente.'
        server_log(msg)
        conn.send(msg.encode('utf-8'))

        msg = 'Opciones disponibles:\n' \
            '1. Ver todos los documentos\n' \
            '2. Buscar un documento por nombre\n' \
            '3. Insertar un nuevo documento\n' \
            '4. Salir'
        conn.send(msg.encode('utf-8'))
        server_log("Opciones enviadas al cliente: {}".format(msg))
        


    except Exception as e:
        server_error(f"Error al conectar a MongoDB: {e}")
        return