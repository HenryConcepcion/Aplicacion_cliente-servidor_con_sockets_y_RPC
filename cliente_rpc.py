import xmlrpc.client

cliente = xmlrpc.client.ServerProxy("http://localhost:8000/")

numero = int(input("Digite un numero entero: "))

resultado = cliente.cuadrado(numero)

print(f"El cuadrado de {numero} es {resultado}")
