import socket, threading, random, time
# networking is not a module, it is a py file containing a string ip and int port number
from networking import port, ip

def gen_message():
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
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        flag = 'not the real flag, but nice try'
        send_flag = True
        i = 0
        start_time = time.time()
        elapsed = time.time()
        while i < 10000 and elapsed - start_time < 20:
            elapsed = time.time()
            try:
                send_message, answer = gen_message()
                try:
                    client.send(send_message)
                except:
                    print('Client disconnected')
                encoded_submission = client.recv(1024)
                if encoded_submission:
                    if grade(encoded_submission, answer) is True:
                        print('correct')
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
        else:
            client.close()

if __name__ == "__main__":
    ThreadedServer('',port).listen()


