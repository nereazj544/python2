import socket
# from Logs import client_log, client_error, client_warning, client_debug, client_critical

HOST = "localhost"  # Dirección del servidor
PORT = 1029

try:
    # client_log("Iniciando conexión con el servidor")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    # client_log("Conexión establecida con el servidor")
except socket.error as e:
    # client_error(f"Error al conectar con el servidor: {e}")
    print(f"Error al conectar con el servidor: {e}")
    exit(1)




while True:
    msg = input("Ingrese un comando: \nEmpresa\nPersonaje\nLenguaje\nSalir\n")


    if msg.lower() == "salir":
        # client_log("Cerrando conexión")
        print("Cerrando conexión")
        break
    elif msg.lower() == "empresa":
        # client_log("Seleccionada la colección Empresa")
        s.sendall(msg.encode())
        while True:
            data = s.recv(1024).decode()
            print("> Servidor dice:", data)
            cmd = input("Ingrese un comando (insertar, consultar, salir): ")
            cmd = cmd.lower()
            if cmd == "insertar":
                s.sendall(cmd.encode())
                data = input("Ingrese los datos de la empresa (nombre): ")
                s.sendall(data.encode())
                response = s.recv(1024).decode()
                print("> Servidor dice:", response)
            elif cmd == "consultar":
                s.sendall(cmd.encode())
                data = input("Ingrese el nombre de la empresa a consultar: ")
                s.sendall(data.encode())
                response = s.recv(1024).decode()
                print("> Servidor dice:", response)
            elif cmd == "salir":
                print("Saliendo de la colección Empresa")
                break
            else:
                print("Comando no reconocido en la colección Empresa")
