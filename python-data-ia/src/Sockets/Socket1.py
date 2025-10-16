import socket

mi_socket = socket.socket()

mi_socket.bind(('localhost', 8000))

mi_socket.listen(5)

while True:
    conexion, addr = mi_socket.accept()
    print('Nueva conx')
    print(addr)
    mensaje = b'Hola dsde el servidor'
    conexion.send(mensaje)
    conexion.close()