import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 4444

client_socket.connect(('192.168.1.36', port))

i = 0
while True:
    message = client_socket.recv(1024)

    answer = message.decode('ascii')
    print(str(answer))

    client_socket.send(answer.encode('ascii'))

    i = i + 1
