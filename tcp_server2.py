import socket, operator, random, logging
from networking import ip

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 4444

server_socket.bind((ip, port))

server_socket.listen(20)


def gen_message():
    string_operators = ['+', '-', '*', '/']
    rand_string_operator = random.choice(string_operators)

    number_1 = random.randint(1, 10) # to be chosen randomly
    number_2 = random.randint(1, 10) # also randomly

    if rand_string_operator == '+':
        answer = number_1 + number_2
    elif rand_string_operator == '-':
        answer = number_1 - number_2
    elif rand_string_operator == '*':
        answer = number_1 * number_2
    elif rand_string_operator == '/':
        answer = number_1 / number_2

    message = str(number_1) + " " + str(rand_string_operator) + " " + str(number_2) + " = ?:" + "\r\n"
    return message, answer

def talk(message):
    try:
        client_socket.send(message.encode('ascii'))
    except IOError:
        print("connection closed")

def recv():
    try:
        encoded_submission = client_socket.recv(1024)
        submission = encoded_submission.decode('ascii')
        print(str(submission))
        return submission
    except:
        print("closed, can't send")

def grade(submission, answer):
    if answer is not submission:
        return False

correct = True
while True:
    client_socket, address = server_socket.accept()
    print("received connection from %s" % str(address))

    sender, correct_answer = gen_message()
    talk(sender)
    blue_submission = recv()
    if grade(blue_submission, correct_answer) is False:
        correct = False