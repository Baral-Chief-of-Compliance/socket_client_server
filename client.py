import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9090))

while True:
    message = (sock.recv(4000)).decode()
    print('server: ', message)
    message = input("Me: ")
    sock.send(message.encode())

