import socket


TCP_IP = '192.168.1.36'
TCP_PORT = 4444
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#s.send(MESSAGE)

data = s.recv(BUFFER_SIZE)
#if not data: break
print(data)
#s.close()
data2 = data[101: 110: 1]
data2 = data2[:-1]

print(data2)
result = str(eval(data2))
s.send(result)
print(result)

while 1:

    data = s.recv(BUFFER_SIZE)
    if not data: break
    print(data)
    #s.close()
    data2 = data[0: 10: 1]
    data2 = data2[:-2]

    print(data2)
    result = str(eval(data2))
    s.send(result)
    print(result)


