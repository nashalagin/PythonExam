import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.connect((host, port)) # подключаемся к серверу
print("Connection to {}:{}".format(host, port))
msg = input()
while msg != 'q':
    s.send(msg.encode())
    resp = s.recv(1024)
    msg = resp.decode()
    print("Response server: " + msg)
    msg = input()
s.close()