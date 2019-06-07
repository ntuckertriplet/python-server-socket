"""
DO NOT USE THIS, IT IS ABSOLUTE TRASH
I didn't think ahead about this at all, I just tried tacking on a bunch of stuff
It doesn't work even remotely, see tcp_server_2.py
"""



# import socket, operator, random, logging
# from networking import ip

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = socket.gethostname()
# port = 4444

# server_socket.bind((ip, port))

# server_socket.listen(20)

# while True:
#     client_socket, address = server_socket.accept()
#     print("received connection from %s" % str(address))

#     # operators = [operator.add, operator.sub, operator.mul]
#     # random_operator = random.choice(operators)

#     correct = True

#     while correct:
#         def gen_message():
#             string_operators = ['+', '-', '*', '/']
#             rand_string_operator = random.choice(string_operators)

#             number_1 = random.randint(1, 10) # to be chosen randomly
#             number_2 = random.randint(1, 10) # also randomly

#             if rand_string_operator == '+':
#                 answer = number_1 + number_2
#             elif rand_string_operator == '-':
#                 answer = number_1 - number_2
#             elif rand_string_operator == '*':
#                 answer = number_1 * number_2
#             elif rand_string_operator == '/':
#                 answer = number_1 / number_2

#             message = str(number_1) + " " + str(rand_string_operator) + " " + str(number_2) + " = ?:" + "\r\n"
            
#             return message

#         def talk(message):
#             try:
#                 client_socket.send(message.encode('ascii'))
#             except IOError:
#                 print("connection closed")

#         def recv():
#             try:
#                 encoded_submission = client_socket.recv(1024)
#                 submission = encoded_submission.decode('ascii')
#                 print(str(submission))
#             except:
#                 print("closed, can't send")

#         def grade(submission):
#             if answer is not submission:
#                 correct = False

#         talk(gen_message())
#         recv()
#         grade(submission)

        
        
        



