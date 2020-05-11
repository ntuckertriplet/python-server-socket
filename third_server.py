import socket, threading, random, time, base64
# networking is not a module, it is a py file containing a string ip and int port number
from networking import port, ip

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

def gen_english_message():
    string_operators = ['plus', 'minus', 'times', 'divided by']
    rand_string_operator = random.choice(string_operators)
    number_1 = random.randint(1, 10) # to be chosen randomly
    number_2 = random.randint(1, 10) # also randomly
    if rand_string_operator == 'plus':
        answer = number_1 + number_2
    elif rand_string_operator == 'minus':
        answer = number_1 - number_2
    elif rand_string_operator == 'times':
        answer = number_1 * number_2
    elif rand_string_operator == 'divided by':
        answer = number_1 / number_2
    message = str(number_1) + " " + str(rand_string_operator) + " " + str(number_2) + " equals ?:" + "\r\n"
    return message, answer

def gen_random_message(option):
    if option is 0:
        message, answer = gen_message()
    else:
        message, answer = gen_english_message()

    return message, answer

def grade(submission, answer):
    try:
        if int(submission) == int(answer):
            return True
        else:
            return False
    except:
        print("empty submission")
        return False

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(15)
        while True:
            client, address = self.sock.accept()
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        flag = 'not the real flag, but nice try'
        send_flag = True
        i = 0
        start_time = time.time()
        elapsed = time.time()
        while i < 10000 and elapsed - start_time < 35:
            elapsed = time.time()
            try:
                rand_message = random.randint(0, 1)
                rand_encoding = random.randint(0, 3)
                send_message, answer = gen_random_message(rand_message)
                try:
                    if rand_encoding is 0:
                        print('no encoding')
                        client.send(send_message)
                    elif rand_encoding is 1:
                        print('ascii')
                        client.send(send_message.encode('ascii'))
                    elif rand_encoding is 2:
                        print('base64')
                        encoded = base64.b64encode(send_message)
                        client.send(encoded + '\r\n')
                    elif rand_encoding is 3:
                        print('base32')
                        encoded = base64.b32encode(send_message)
                        client.send(encoded + '\r\n')
                except:
                    print('Client disconnected')
                encoded_submission = client.recv(1024)
                if encoded_submission:
                    if grade(encoded_submission, answer) is True:
                        i += 1
                    else:
                        send_flag = False
                        client.close()
                        print('incorrect')
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False
        if i == 10000 and send_flag is True:
            print('sending flag')
            client.send(flag)
            client.close()

if __name__ == "__main__":
    ThreadedServer('',port).listen()


