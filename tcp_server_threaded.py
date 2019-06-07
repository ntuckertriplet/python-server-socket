import socket, threading, random
from networking import *

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
        clientsock.send(message.encode('ascii'))
    except:
        print("connection closed, can't send")

def recv():
    try:
        encoded_submission = clientsock.recv(1024)
        submission = encoded_submission.decode('ascii')
        return submission
    except:
        print("closed, can't receive")

def grade(submission, answer):
    try:
        if int(submission) == int(answer):
            print("correct")
            return True
        else:
            print("false")
            return False
    except:
        print("empty submission")
        return False

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        while True:
            send_message, answer = gen_message()
            print(send_message)
            talk(send_message)
            input_submission = recv()
            print(input_submission)
            if grade(input_submission, answer) == False:
              print("incorrect answer")
              break
        print ("Client at ", clientAddress , " disconnected...")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, port))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(20)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()