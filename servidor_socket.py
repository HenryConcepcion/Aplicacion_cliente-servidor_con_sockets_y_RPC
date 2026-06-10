import socket

HOST = '127.0.0.1'
PORT = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen(1)

print("Servidor esperando conexiones...")

conexion, direccion = servidor.accept()

print(f"Conectado con {direccion}")

mensaje = conexion.recv(1024).decode()

print("Mensaje recibido:", mensaje)

respuesta = "Mensaje recibido correctamente"
conexion.send(respuesta.encode())

conexion.close()
servidor.close()
