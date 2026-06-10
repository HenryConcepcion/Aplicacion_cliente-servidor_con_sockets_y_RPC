import socket

HOST = '127.0.0.1'
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

mensaje = "Hola servidor"

cliente.send(mensaje.encode())

respuesta = cliente.recv(1024).decode()

print("Respuesta del servidor:", respuesta)

cliente.close()
