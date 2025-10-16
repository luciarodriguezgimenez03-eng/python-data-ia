import socket
mi_socket = socket.socket()

mi_socket.connect(('localhost', 8000))
mensaje = b'Hola desde el cliente'
longitud = len(mensaje)

mi_socket.send(mensaje)
respuesta = mi_socket.recv(1024)

print(respuesta)
mi_socket.close()