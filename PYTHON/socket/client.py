import socket
HOST = "127.0.0.1"
PORT = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket TCP/IP

s.connect((HOST, PORT))

while "Exit":  
    data = s.recv(1024).decode()  # Recibe la respuesta del servidor
    print(f"Respuesta del servidor: {data}")  # Imprime la respuesta del servidor
    # Bucle para enviar mensajes hasta que se envíe "Exit"
    msg = input("Escribe un mensaje (o 'e x i t' para salir): ")  # Solicita al usuario un mensaje
    
    if msg.lower() == "exit":  # Si el usuario escribe "Exit", se sale del bucle
        break
    s.sendall(msg.encode())  # Envía el mensaje al servidor


s.close()  # Cierra el socket