import socket, threading, random
from networking import *

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        print ("Connection from : ", clientAddress)

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
            except:
                print("connection closed, can't send")

        def recv():
            try:
                encoded_submission = client_socket.recv(1024)
                submission = encoded_submission.decode('ascii')
                print(str(submission))
                return submission
            except:
                print("closed, can't receive")

        def grade(submission, answer):
            try:
                print("submission:"+str(submission)+" answer:"+str(answer))
                if int(submission) == int(answer):
                    print("correct")
                    return True
                else:
                    print("false")
                    return False
            except:
                print("empty submission")
                return False

        while True:
            send_message, answer = gen_message()
            talk(send_message)
            input_submission = recv()
            if grade(input_submission, answer) == False:
              break
            print ("from client", input_submission)
        print ("Client at ", clientAddress , " disconnected...")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, port))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()