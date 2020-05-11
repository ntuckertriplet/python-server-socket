import socket, threading, random, time, base64


def gen_message():
    string_operators = ['+', '-', '*', '/', 'plus', 'minus', 'times', 'divided by']
    rand_string_operator = random.choice(string_operators)
    number_1 = random.randint(1, 10)  # to be chosen randomly
    number_2 = random.randint(1, 10)  # also randomly
    if rand_string_operator == '+' or rand_string_operator == 'plus':
        answer = number_1 + number_2
    elif rand_string_operator == '-' or rand_string_operator == 'minus':
        answer = number_1 - number_2
    elif rand_string_operator == '*' or rand_string_operator == 'times':
        answer = number_1 * number_2
    elif rand_string_operator == '/' or rand_string_operator == 'divided by':
        answer = number_1 // number_2
    message = str(number_1) + " " + str(rand_string_operator) + " " + str(number_2) + " = ?:" + "\r\n"
    return message, answer


def grade(submission, answer):
    if int(submission) == int(answer):
        return True

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
            threading.Thread(target=self.listenToClient, args=(client, address)).start()

    def listenToClient(self, client, address):
        flag = 'TEST FLAG'
        send_flag = True
        i = 0
        start_time = time.time()
        elapsed = time.time()
        while i < 1000 and elapsed - start_time < 35:
            elapsed = time.time()
            rand_encoding = random.randint(0, 3)
            send_message, answer = gen_message()

            if rand_encoding is 2:
                print('base64')
                send_message = base64.b64encode(send_message.encode('ascii'))
            elif rand_encoding is 3:
                print('base32')
                send_message = base64.b32encode(send_message.encode('ascii'))
            else:
                print('ascii')
                send_message = send_message.encode('ascii')

            try:
                client.send(send_message)
                encoded_submission = client.recv(1024)
                if encoded_submission == b'\n':
                    client.send(b'empty answer')
                    client.close()

                if grade(encoded_submission, answer) is True:
                    i += 1
                else:
                    send_flag = False
                    client.send(b'incorrect answer')
                    client.close()
                    print('incorrect')
            except Exception as e:
                client.close()
                print(e)
                return False

        if i == 1000 and send_flag is True:
            print('sending flag')
            client.send(flag.encode('ascii'))
            client.close()


if __name__ == "__main__":
    ThreadedServer('', 4446).listen()
