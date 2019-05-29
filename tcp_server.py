import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 4444

server_socket.bind(('192.168.1.36', port))

server_socket.listen(20)

while True:
    client_socket, address = server_socket.accept()

    print("received connection from %s" % str(address))

    message = "thank you for connecting " + "\r\n"
    client_socket.send(message.encode('ascii'))

    client_socket.close()

