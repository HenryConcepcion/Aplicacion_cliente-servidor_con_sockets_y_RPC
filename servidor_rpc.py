from xmlrpc.server import SimpleXMLRPCServer

def cuadrado(numero):
    return numero * numero

servidor = SimpleXMLRPCServer(("localhost", 8000))

print("Servidor RPC iniciado...")

servidor.register_function(cuadrado, "cuadrado")

servidor.serve_forever()
