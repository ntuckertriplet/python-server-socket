import socket, operator, random, logging, os, time
from networking import ip, port

"""
This block sets up the listener and all of the server-side operations using IPV4
the .listen(20) means a maximum of 20 connections at a time
"""
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
server_socket.bind((ip, port))
server_socket.listen(20)

"""
This is the block that generates the math problem to solve and the answer to that problem
"""
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
    correct = True
    flag = "cdc"

    client_socket, address = server_socket.accept()
    print("received connection from %s" % str(address))

    i = 0

    while correct is True and i < 4000:
        seconds = 0
        sender, correct_answer = gen_message()
        print(str(sender) + " is " + str(correct_answer))
        talk(sender)
        blue_submission = recv()
        if grade(blue_submission, correct_answer) == False:
            correct = False
        i += 1
        if i == 4000:
            client_socket.send(flag.encode('ascii'))
            print("sending flag")