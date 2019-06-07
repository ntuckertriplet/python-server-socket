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

"""
This is the driver code. I want the server to always run, hence the while
"""
while True:
    correct = True
    flag = "cdc{I_hope_you_scripted_this}"

    # Initiate the connection, as well as where it came from
    client_socket, address = server_socket.accept()
    print("received connection from %s" % str(address))

    i = 0

    # Default to correct answers until an incorrect one is submitted, or they reach the end
    while correct is True and i < 1000000:
        # the sender is the encoded math problem that will be sent to the blue team, the correct answer is just that
        sender, correct_answer = gen_message()

        # debugging code. print the sender problem and the answer to the problem
        print(str(sender) + " is " + str(correct_answer))

        # this method takes in the sender and sends it
        talk(sender)

        #receive the blue submission with this call
        blue_submission = recv()

        # pass in the submission and answer, check if they are the same. If not, stop the while, stop sending
        if grade(blue_submission, correct_answer) == False:
            correct = False
        i += 1

        # they were right an insane number of times, send the flag
        if i == 1000000:
            client_socket.send(flag.encode('ascii'))
            print("sending flag")