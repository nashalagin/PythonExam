import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1' # '127.0.0.1' соответствует хосту, на котором запускается скрипт
port = 12345
s.bind((host, port))
s.listen(5) # Открываем порт на сервере (не более 5 клиентов одновременно)
while True:
    conn, addr = s.accept()
    print('Server got connection from {}'.format(addr))
    req = conn.recv(1024)
    msg = req.decode()
    conn.send(msg.encode())
    conn.close()
