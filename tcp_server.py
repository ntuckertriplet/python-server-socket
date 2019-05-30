import socket, operator, random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 4444

server_socket.bind(('192.168.1.36', port))

server_socket.listen(20)

while True:
    client_socket, address = server_socket.accept()

    print("received connection from %s" % str(address))

    # operators = [operator.add, operator.sub, operator.mul]
    # random_operator = random.choice(operators)

    string_operators = ['+', '-', '*', '/']
    rand_string_operator = random.choice(string_operators)

    number_1 = random.randint(1, 10) # to be chosen randomly
    number_2 = random.randint(1, 10) # also randomly
    message = str(number_1) + " " + str(rand_string_operator) + " " + str(number_2) + " = ?:" + "\r\n"
    client_socket.send(message.encode('ascii'))


