import socket


TCP_IP = '10.126.161.151'
TCP_PORT = 4444
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

flag_received = False
while flag_received is False:
    data = s.recv(BUFFER_SIZE)
    submission = data.decode('ascii')
    final = submission.split(' ')
    del final[3:]
    print(submission)
    try:
        answer = str(eval(''.join(final)))
        print(str(answer))
        s.send(answer.encode('ascii'))
    except:
        flag_received = True
        s.close()