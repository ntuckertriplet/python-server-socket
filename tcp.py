import socket


TCP_IP = '206.189.224.72'
TCP_PORT = 5123
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#s.send(MESSAGE)

data = s.recv(BUFFER_SIZE)
#if not data: break
print data
#s.close()
data2 = data[0: 10: 1]
data2 = data2[:-3]

print data2
result = str(eval(data2))
s.send(result + "\n")
print result

i = 0

while i < 24:

    data = s.recv(BUFFER_SIZE)
    if not data: break
    print data
    #s.close()
    data2 = data[0: 10: 1]
    data2 = data2[:-3]
    
    print data2
    result = str(eval(data2))
    s.send(result + "\n")
    print result
    print i
    i += 1

while 1:
    data = s.recv(BUFFER_SIZE)
    if not data: break
    print data
    newdata = data.split(' ')
    if newdata[1] == 'plus':
        result = int(newdata[0]) + int(newdata[2])
        print result

    elif newdata[1] == 'minus':
        result = int(newdata[0]) - int(newdata[2])
        print result

    elif newdata[1] == 'mod':
        result = int(newdata[0]) % int(newdata[2])
        print result

    elif newdata[1] == 'times':
        result = int(newdata[0]) * int(newdata[2])
        print result

    elif newdata[1] == 'divided':
        result = int(newdata[0]) / int(newdata[3])
        print result

    s.send(str(result) + '\n')
    i += 1
    print i


